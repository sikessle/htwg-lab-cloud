import requests, json, xml.etree.ElementTree as ET

def main():
	#print(get_enrolled_students(1149, get_user_token()))
	#print(get_user_courses(3701, get_user_token()))
	userid = get_moodle_user_id('eck@htwg-konstanz.de', token)

	courses = get_user_courses(userid, get_user_token())

	for id in courses:
		print id + ":" + courses[id]

	users = get_enrolled_students(1149, get_user_token())

	for user in users:
		print user

def get_user_token():
	ldap_userid = 'htwgapp'
	password = '@@@adminmoodlepw@@@'
	moodle_url = "https://moodle.htwg-konstanz.de/moodle/login/token.php"
	parameter = {'username':ldap_userid, 'password':password, 'service':'htwgapp'}
	response = requests.post(moodle_url, params=parameter)

	response_content = json.loads(response.text)

	token = response_content['token']

	return token

def get_moodle_user_id(ldap_user_email, token):
	moodle_url = "https://moodle.htwg-konstanz.de/moodle/webservice/rest/server.php"
	parameter = {'wstoken':token, 'wsfunction':'core_user_get_users', 'criteria[0][key]':'email', 'criteria[0][value]':ldap_user_email + '@htwg-konstanz.de'}
	response = requests.post(moodle_url, params=parameter)

	response_root = ET.fromstring(response.content)

	for user in response_root.iter('KEY'):
		attr = user.get('name')

		if attr == 'id':
			return int(user.find('VALUE').text)

	return -1

def get_course_data(course_id, token):
	moodle_url = "https://moodle.htwg-konstanz.de/moodle/webservice/rest/server.php"
	parameter = {'wstoken':token, 'wsfunction':'core_enrol_get_enrolled_users', 'courseid':course_id}
	response = requests.post(moodle_url, params=parameter)

	return ET.fromstring(response.content)

def is_prof_of_course(course_id, moodle_userid, token):
	response_root = get_course_data(course_id, token)

	userid = -1
	roleid = -1

	for user in response_root.iter('KEY'):
		attr = user.get('name')

		if attr == 'id':
			userid = int(user.find('VALUE').text)

		if attr == 'roleid':
			roleid = int(user.find('VALUE').text)

			#roleid 3 Dozent, roleid 5 Studierende
			if userid == moodle_userid and roleid == 3:
				return True

	return False

def get_user_courses(moodle_userid, token):

	moodle_url = "https://moodle.htwg-konstanz.de/moodle/webservice/rest/server.php"
	parameter = {'wstoken':token, 'wsfunction':'core_enrol_get_users_courses', 'userid':moodle_userid}
	response = requests.post(moodle_url, params=parameter)

	response_root = ET.fromstring(response.content)

	course_data = {}

	for course in response_root.iter('SINGLE'):
		course_id = -1
		course_shortname = ""
		course_fullname = ""

		for attribute in course.iter('KEY'):
			attr = attribute.get('name')

			if attr == 'id':
				course_id = int(attribute.find('VALUE').text)

			elif attr == 'shortname':
				course_shortname = attribute.find('VALUE').text

			elif attr == 'fullname':
				course_fullname = attribute.find('VALUE').text

				if is_prof_of_course(course_id, moodle_userid, token):

					if course_id not in course_data:
						course_data[course_id] = {}
						course_data[course_id]['shortname'] = course_shortname
						course_data[course_id]['fullname'] = course_fullname

	return course_data

def get_enrolled_students(course_id, token):
	response_root = get_course_data(course_id, token)

	student_data = {}

	student_name = ""
	student_email = ""

	for student in response_root.iter('KEY'):
		attr = student.get('name')

		if attr == 'fullname':
			student_name = student.find('VALUE').text

		elif attr == 'email':
			student_email = student.find('VALUE').text

		elif attr == 'roleid':
			roleid = int(student.find('VALUE').text)

			#roleid 3 Dozent, roleid 5 Studierende
			if type(student_email) is str and roleid == 5:
				student_data[student_email] = student_name

				student_name = ""
				student_email = ""

	return student_data

if __name__ == "__main__":
	main()
