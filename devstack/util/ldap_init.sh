sed -i "s/^driver = keystone.identity.backends.sql.Identity/driver = keystone.identity.backends.ldap.Identity/g" /etc/keystone/keystone.conf

sed -i "/^\[ldap\]/r ./ldap_keystone_config.txt" /etc/keystone/keystone.conf

sudo service apache2 restart

sudo apt-get install -y python-pip
sudo apt-get install -y python-ldap
sudo pip install ldappool
sudo pip install Django

sleep 10

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 21347 --role admin --tenant admin

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 21347 --role admin --tenant demo

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 21347 --role admin --tenant service

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ tenant-create --name professor

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 21347 --role admin --tenant professor

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 19079 --role service --tenant service

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 12434 --role service --tenant service

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 29005 --role service --tenant service

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 28072 --role service --tenant service

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 19445 --role service --tenant service

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 23961 --role service --tenant service

keystone --os-endpoint http://10.0.2.15:35357/v2.0 --os-token @@@adminpw@@@ user-role-add --user-id 19799 --role service --tenant service

python ./add_prof_tenants.py
