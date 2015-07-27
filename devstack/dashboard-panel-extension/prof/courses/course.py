import time
import inspect
from client import Admin
from moodle import get_user_courses
from moodle import get_enrolled_students
from django.core.mail import send_mail

class Course:
    """
    Course class represents the course data
    """
    def __init__(self, name, id, description):
        self.name = name
        self.id = id
        self.description = description

class CourseHelper:
    """
    Helper class to create Openstack tenants based on moodle courses.
    """
    def __init__(self, user):
        self.user = user
        self.client = Admin()
        self.actualTenant = None
        self.switchTenant('demo')

    # helper method to switch the tenant. Instances will be started for a tenant. 
    # To start or stop instances we need to switch to the tenant
    def switchTenant(self, name=None):
        if self.actualTenant != name:
            self.actualTenant = name
            self.keystone = self.client.keystone(self.actualTenant)
            self.nova = self.client.nova(self.actualTenant)
            self.cinder = self.client.cinder(self.actualTenant)

    # get a course by a id
    def getCourse(self, id):
        courses = self.getCourses()
        for course in courses:
            if (course.id == id):
                return course
        # course not exist
        raise Exception('Course does not exist', id)

    # get all courses by loading moodle courses and creating a tenant for each non existing course.
    def getCourses(self):
        moodleCourses = self.__getMoodleCourses()
        tenants = self.__getTenants()

        # create a course for each
        for course in moodleCourses:
            if course.id not in tenants:
                self.__addCourse(course)
        return moodleCourses
    
    # load moodle courses and return all of them in a list.
    def __getMoodleCourses(self):
        list = []        
        # TODO : replace token with token=self.user.token.id
        moodleCourses = get_user_courses(moodle_userid=3701, token="32c2fad270a6ca8ff1d712c62e37822c")
        for moodleId in moodleCourses:
            list.append(Course(name=moodleCourses[moodleId]['shortname'], id=moodleId, description=moodleCourses[moodleId]['fullname']))
        return list
    
    # load a list with all tenants
    def __getTenants(self):
        list = []
        tenants = self.keystone.tenants.list()
        for tenant in tenants:
            list.append(tenant.id)
        #print self.keystone.roles.list()
        return list

    # add a course
    def __addCourse(self, course):
        # Create the course
        tenant = self.keystone.tenants.create(id=course.id, tenant_name=course.name, description=course.description)
        # get the Member role.
        role = self.keystone.roles.find(name="admin")

        # TODO : enable if LDAP is running. add the course owner to the tenant  
        # user = self.keystone.users.find(id=self.user.id)
        # self.keystone.roles.add_user_role(user, role, tenant)
        # Add the admin to the role.
        admin = self.keystone.users.find(id=self.keystone.session.get_user_id())
        self.keystone.roles.add_user_role(admin, role, tenant)

        # now the tenant exist, we need to switch to the new created tenant. Otherwise we would add security settings to
        # another active tenant.        
        self.switchTenant(course.name)
        # Add the security group rules for the created tenant to the default security group
        # Therefore we need the default one.
        group = None

        for groups in self.nova.security_groups.list():
            if groups.tenant_id == tenant.id and groups.name == "default":
                group = groups
                break
        if not group:
            group = self.nova.security_groups.create(name="default", description="default")
        self.nova.security_group_rules.create(parent_group_id=group.id, ip_protocol="tcp", from_port=1, to_port=65535, cidr="0.0.0.0/0")
        self.nova.security_group_rules.create(parent_group_id=group.id, ip_protocol="udp", from_port=1, to_port=65535, cidr="0.0.0.0/0")
        self.nova.security_group_rules.create(parent_group_id=group.id, ip_protocol="icmp", from_port=-1, to_port=-1, cidr="0.0.0.0/0")

    # refresh will execute startInstances again. startInstance will only start an instance for users which doesn't already have one.
    # method is useful if the moodle course get some new members which require a maschine with the same image of the course.
    def refreshInstances(self, courseId=None):
        course = self.getCourse(courseId)
        self.switchTenant(course.name)
        servers = self.nova.servers.list()
        if servers:
            self.startInstances(courseId, imageId=servers[0].image["id"], flavorId=servers[0].flavor["id"])

    # stop all instances for a specific course. 
    # This method will terminate each instance and delete each blockstorage for the provided course.
    def stopInstances(self, courseId=None):
        course = self.getCourse(courseId)
        self.switchTenant(course.name)
        print "stop instances"
        # stop running instances
        servers = self.nova.servers.list()
        for server in servers:
            if (server.name.startswith(courseId)):
                print "Stop Server " + server.name
                server.delete()
        # remove volumes.
        volumes = self.cinder.volumes.list()
        for volume in volumes:
            if (volume.name.startswith(courseId)):
                print "Remove Volume " + volume.name
                # if volume is still attached we need to detach
                if (volume.status == "in-use"):             
                    volume.detach()
                volume.delete()

    # start all instances for a specific course. 
    # This method will start one instance and create one blockstorage for each member of the course
    def startInstances(self, courseId=None, imageId=None, flavorId=None):
        course = self.getCourse(courseId)
        self.switchTenant(course.name)
        # TODO : replace token with token=self.user.token.id
        #members = get_enrolled_students(course_id=courseId, token="32c2fad270a6ca8ff1d712c62e37822c")
        members = ['studentA', 'studentB']                
        for member in members:
            name = courseId + "-" + member
            if not self.nova.servers.list(search_opts={'name': name}):
                self.__startInstance(instanceName=name, imageId=imageId, flavorId=flavorId)
                self.__sendVncConsole(course, student=member, instanceName=name)
            if not self.cinder.volumes.list(search_opts={'name': name}):
                self.cinder.volumes.create(name=name, size=1)
            # from this point instance and volume should exist
            # get the instance and attach the volume to it.
            instance = self.nova.servers.list(search_opts={'name': name})        
            volume = self.cinder.volumes.list(search_opts={'name': name})
            # check the state of the volume to check if we need to attach it.
            print "Volume " + volume[0].name + " is " + volume[0].status
            # check if we need to attach the volume.
            if (volume[0].status == "creating" or volume[0].status == "available"):
                # It's possible that there are multiple instances/volumes with the same name.
                # We just use the first one.
                attached = self.cinder.volumes.attach(volume[0], instance[0].id, "/dev/vdb", mode="rw")

    # helper method to send the VNC Access credentials to each student.
    def __sendVncConsole(self, course=None, student="studentEmail", instanceName="courseId-studentEmail"):
        print "Try to send vnc for " + instanceName
        #get the instance
        servers = self.nova.servers.list(search_opts={'name': instanceName})
        if servers:
            try:
                sender = 'cloud@htwg-konstanz.de'
                receiver = student
                message = ""
                message += "Welcome to HTWG Cloud.\n"
                message += "This is your link to access your virtual machine\n"
                message += "Course : " + course.name + " - " + course.description + "\n"
                message += "Link : " + servers[0].get_vnc_console(console_type="novnc")["console"]["url"] + "\n"
                print "SendMail " + receiver
                send_mail('HTWG Cloud - ' + course.name, message, sender, [receiver], fail_silently=False)
            except:
                print 'sendVncConsole failed'
                
    # helper method to start a single instance
    def __startInstance(self, instanceName="courseId-studentEmail", imageId=None, flavorId=None):
        # find the image we like to use
        image = self.nova.images.find(id=imageId)
        # find the flavor we like to use
        flavor = self.nova.flavors.find(id=flavorId)
        # create the instance
        instance = self.nova.servers.create(name=instanceName, image=image, flavor=flavor)

        # Poll at 5 second intervals, until the status is no longer 'BUILD'
        status = instance.status
        while status == 'BUILD':
            time.sleep(5)
            # Retrieve the instance again so the status field updates
            instance = self.nova.servers.get(instance.id)
            status = instance.status
            print "status: %s" % status
