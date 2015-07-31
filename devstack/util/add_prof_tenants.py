import ldap, json
from string import ascii_uppercase
from subprocess import call

def main():
    print(get_prof_data_ldap())

def create_projects():
    prof_ids = get_prof_data_ldap()
    for ldap_id in prof_ids:
        call(["keystone", "--os-endpoint", "http://10.0.2.15:35357/v2.0", "--os-token", "@@@adminpw@@@", "user-role-add", "--user-id", ldap_id, "--role", "Member", "--tenant", "professor"])

def get_prof_data_ldap():
    uid_list = []

    for c in ascii_uppercase:
        get_prof_data_ldap_startletter(c, uid_list)

    return uid_list

def get_prof_data_ldap_startletter(startletter, uid_list):
    try:
        ld = ldap.initialize('ldap://ldap.htwg-konstanz.de:389')

        ld.simple_bind_s()

        basedn = "ou=users,dc=fh-konstanz,dc=de"

        filter = "(&(gidNumber=121)(sn=" + startletter +"*))"

        results = ld.search_s(basedn, ldap.SCOPE_SUBTREE, filter)

        for entry in results:
            uid_list.append(int((entry[1].get('uidNumber', 0))[0]))

    except ldap.LDAPError, error:
        print ('problem with ldap', error)

if __name__ == "__main__":
    main()