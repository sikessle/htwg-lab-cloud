import time
import inspect
from client import Admin

class Course:
    """
    Course class represents the course data
    """
    def __init__(self, name, description, id, enabled):
        self.name = name
        self.description = description
        self.id = id
        self.enabled = enabled
        # TODO : set email of course owner here.
        self.owner = "test@test.de"
        # TODO : set list of all course members
        self.members = ["student1@test.de", "studen2@test.de"]

class CourseHelper:
    """
    Helper class to create Openstack tenants based on moodle courses.
    """
    def __init__(self):
        client = Admin()
        self.keystone = client.keystone()
        self.glance = client.glance()
        self.nova = client.nova()
        self.cinder = client.cinder()

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
        list.append(Course(name="WebTech", description="WebTechnologien", id="1", enabled="Yes"))
        list.append(Course(name="DBSYS", description="Datenbanksysteme", id="2", enabled="No"))
        list.append(Course(name="CloudAppDev", description="Cloud Application Development", id="3", enabled="No"))
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
            role = self.keystone.roles.find(name="Member")
            # get the owner of the course
            user = self.keystone.users.find(email=course.owner)
            # add the course owner to the tenant      
            self.keystone.roles.add_user_role(user, role, tenant)
        except:
            print "Unable to set owner of tenant."
        return True

    def stopInstances(self, courseId=None):
        print "stop instances"
        course = self.getCourse(courseId)
        # stop running instances
        servers = self.nova.servers.list()
        for server in servers:
            if (server.name.startswith(course.id)):
                print "Stop Server " + server.name
                server.delete()
        # remove volumes.
        volumes = self.cinder.volumes.list()
        for volume in volumes:
            if (volume.name.startswith(course.id)):
                print "Remove Volume " + volume.name
                # if volume is still attached we need to detach
                if (volume.status == "in-use"):             
                    volume.detach()
                volume.delete()

    def startInstances(self, courseId=None, imageId=None, flavorId=None):
        course = self.getCourse(courseId)
        for member in course.members:
            name = course.id + "-" + member
            if (False == self.__instanceExist(name=name)):
                self.__startInstance(instanceName=name, imageId=imageId, flavorId=flavorId)
            if (False == self.__volumeExist(name=name)):
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

    def __instanceExist(self, name="courseId-studentEmails"):
        instance = self.nova.servers.list(search_opts={'name': name})
        if not instance:
            return False
        else:
            print "Intance already exist"
            return True

    def __volumeExist(self, name="courseId-studentEmails"):
        volume = self.cinder.volumes.list(search_opts={'name': name})
        if not volume:
            return False
        else:
            print "Volume already exist"
            return True

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

# TODO : remove
# manually start for test.
helper = CourseHelper()
courses = helper.getCourses()
#for course in courses:
#    print course.members
    #helper.startInstances(course=course)
#    helper.stopInstances(course=course)

#helper.startInstances(course=courses[0])
#helper.stopInstances(course=courses[0])
#helper.createVolume()

#print CourseSession.selectedCourse
#CourseSession.selectedCourse = helper.getCourses()[0]
#print CourseSession.selectedCourse

