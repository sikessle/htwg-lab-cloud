import time
import inspect
from client import Admin
from moodle import get_user_courses
from moodle import get_enrolled_students

class Course:
    """
    Course class represents the course data
    """
    def __init__(self, name, id, description):
        self.name = name
        self.id = id
        self.description = description
        self.enabled = True

class CourseHelper:
    """
    Helper class to create Openstack tenants based on moodle courses.
    """
    def __init__(self, user):
        self.user = user
        self.client = Admin()
        self.actualTenant = None
        self.switchTenant('demo')

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

        # create a course for each
        for course in moodleCourses:
            self.__addCourse(course)
        return moodleCourses
    
    # load moodle courses and return all of them in a list.
    def __getMoodleCourses(self):
        list = []        
        # TODO : replace token with token=self.user.token.id
        moodleCourses = get_user_courses(ldap_userid=3701, token="32c2fad270a6ca8ff1d712c62e37822c")
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
        tenants = self.__getTenants()
        # check if the tenant already exist.
        if course.id in tenants:
            return False

        # Create the course
        tenant = self.keystone.tenants.create(id=course.id, tenant_name=course.name, description=course.description, enabled=True)
        # if something goes wrong on setting the owner of the tenant, we do not throw an exception.
        try:
            # get the Member role.
            role = self.keystone.roles.find(name="admin")
            # get the owner of the course
            user = self.keystone.users.find(id=self.user.id)
            # add the course owner to the tenant      
            self.keystone.roles.add_user_role(user, role, tenant)
        except:
            print "Unable to set owner of tenant."
        return True

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

    def __startInstance(self, instanceName="courseId-studentEmail", imageId=None, flavorId=None):
        print "start instance"
        #if not self.nova.keypairs.findall(name="mykey"):
        #    with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
        #        nova.keypairs.create(name="mykey", public_key=fpubkey.read())
        
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

