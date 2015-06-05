import time
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
        print self.keystone.roles.list()
        return list

    # add a course
    def __addCourse(self, course):
        tenants = self.__getTenants()
        # check if the tenant already exist.
        if course.id in tenants:
            return False

        # Create the course
        tenant = self.keystone.tenants.create(id=course.id, tenant_name=course.name, description=course.description, enabled=True)
        # get the Member role.
        role = self.keystone.roles.find(name="Member")
        # get the owner of the course
        user = self.keystone.users.find(email=course.owner)
        # add the course owner to the tenant      
        self.keystone.roles.add_user_role(user, role, tenant)
        return True

    def stopInstances(self, course=None):
        print "stop instances"
        servers = self.nova.servers.list()
        for server in servers:
            if (None != course and server.name.startswith(course.id)):
                print "Stop Server " + server.name
                server.delete()

    def startInstances(self, course=None, imageName="cirros-0.3.4-x86_64-uec", flavorName="m1.tiny"):
        for member in course.members:
            instanceName = course.id + "-" + member
            if (False == self.__instanceExist(name=instanceName)):
                self.__startInstance(instanceName=instanceName, imageName=imageName, flavorName=flavorName)

    def __instanceExist(self, name="courseId-studentEmails"):
        try:
            self.nova.servers.find(name=name)
            print "Instance already exist"
            return True
        except Exception:
            return False

    def __startInstance(self, instanceName="courseId-studentEmail", imageName="cirros-0.3.4-x86_64-uec", flavorName="m1.tiny"):
        print "start instance"
        #if not self.nova.keypairs.findall(name="mykey"):
        #    with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
        #        nova.keypairs.create(name="mykey", public_key=fpubkey.read())
        
        # find the image we like to use
        image = self.nova.images.find(name=imageName)
        # find the flavor we like to use
        flavor = self.nova.flavors.find(name=flavorName)
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
for course in courses:
    print course.members
    #helper.startInstances(course=course)
    helper.stopInstances(course=course)


