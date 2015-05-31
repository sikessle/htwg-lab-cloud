from .client import Client

class Course:
    """
    Course class represents the course data
    """
 
    def __init__(self, name, description, id, enabled):
        self.name = name
        self.description = description
        self.id = id
        self.enabled = enabled

class CourseHelper:
    def __init__(self):
        client = Client()
        self.keystone = client.keystone()
        self.glance = client.glance()
        self.nova = client.nova()
        self.cinder = client.cinder()

    # get all courses by loading moodle courses and creating a tenant for each non existing course.
    def getCourses(self):
        moodleCourses = self.getMoodleCourses()
        
        # create a course for each
        for course in moodleCourses:
            self.addCourse(course)
        return moodleCourses
    
    # load moodle courses and return all of them in a list.
    def getMoodleCourses(self):
        list = []
        list.append(Course(name="WebTech", description="WebTechnologien", id="1", enabled="Yes"))
        list.append(Course(name="DBSYS", description="Datenbanksysteme", id="2", enabled="No"))
        list.append(Course(name="CloudAppDev", description="Cloud Application Development", id="3", enabled="No"))
	list.append(Course(name="ITSecurity", description="IT Security", id="4", enabled="No"))
        return list
    
    # load a list with all tenants
    def getTenants(self):
        list = []
        tenants = self.keystone.tenants.list()
        for tenant in tenants:
            list.append(tenant.id)
        print self.keystone.roles.list()
        return list

    # add a course
    def addCourse(self, course):
        tenants = self.getTenants()
        if course.id in tenants:
            return False
        # Create the course
        tenant = self.keystone.tenants.create(id=course.id, tenant_name=course.name, description=course.description, enabled=True)
        # Create a user and set the role 
        #self.keystone.users.create(name="cloud", password="12345678", email="some@test.de", tenant_id=tenant.id)
        # TODO : check if we need to set a role.        
        # self.keystone.roles.add_user_role(user, role, tenant)
        return True


