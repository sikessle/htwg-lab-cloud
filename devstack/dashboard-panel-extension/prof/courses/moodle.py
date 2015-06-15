import requests, json, xml.etree.ElementTree as ET

def main():
	#print(get_enrolled_students(1149, get_user_token()))
	#print(get_user_courses(3701, get_user_token()))
	courses = get_user_courses(3701, get_user_token())

	for id in courses:
		print id + ":" + courses[id]

	users = get_enrolled_students(1149, get_user_token())

	for user in users:
		print user

def get_user_token():
	token = '32c2fad270a6ca8ff1d712c62e37822c'

	return token

def get_user_courses(ldap_userid, token):

	moodle_url = "https://moodle.htwg-konstanz.de/moodle/webservice/rest/server.php"
	parameter = {'wstoken':token, 'wsfunction':'core_enrol_get_users_courses', 'userid':ldap_userid}
	response = requests.post(moodle_url, params=parameter)

	response_root = ET.fromstring(response.content)

	course_data = {}

	for course in response_root.iter('SINGLE'):
		course_id = -1
		course_name = ""

		for attribute in course.iter('KEY'):
			attr = attribute.get('name')

			if attr == 'id':
				course_id = attribute.find('VALUE').text
				if course_id not in course_data:
					course_data[course_id] = {}
			elif attr == 'shortname':
				course_data[course_id]['shortname'] = attribute.find('VALUE').text

			elif attr == 'fullname':
				course_data[course_id]['fullname'] = attribute.find('VALUE').text

	return course_data

def get_enrolled_students(course_id, token):
	moodle_url = "https://moodle.htwg-konstanz.de/moodle/webservice/rest/server.php"
	parameter = {'wstoken':token, 'wsfunction':'core_enrol_get_enrolled_users', 'courseid':course_id}
	response = requests.post(moodle_url, params=parameter)

	response_root = ET.fromstring(response.content)

	student_data = {}

	student_name = ""
	student_email = ""

	for student in response_root.iter('KEY'):
		attr = student.get('name')

		if attr == 'fullname':
			student_name = student.find('VALUE').text

		elif attr == 'email':
			student_email = student.find('VALUE').text

			if type(student_email) is str:
				student_data[student_email] = student_name

				student_name = ""
				student_email = ""

	return student_data

if __name__ == "__main__":
	main()
