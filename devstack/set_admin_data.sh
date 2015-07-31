ADMINPW=''
ADMINSERVICEPW=''
ADMINMOODLEPW=''

sed -i 's/@@@adminpw@@@/'$ADMINPW'/g' local.conf

sed -i 's/@@@adminservicepw@@@/'$ADMINSERVICEPW'/g' local.conf

sed -i 's/@@@adminpw@@@/'$ADMINPW'/g' util/add_prof_tenants.py

sed -i 's/@@@adminpw@@@/'$ADMINPW'/g' util/ldap_init.sh

sed -i 's/@@@adminpw@@@/'$ADMINPW'/g' util/instance.py

sed -i 's/@@@adminpw@@@/'$ADMINPW'/g' dashboard-panel-extension/prof/courses/client.py

sed -i 's/@@@adminmoodlepw@@@/'$ADMINMOODLEPW'/g' dashboard-panel-extension/prof/courses/moodle.py
