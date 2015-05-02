#!/bin/sh

if [ "$(whoami)" != "root" ]; then
	echo "root/sudo required. Stopping."
	exit 1
fi

echo "installing ldap packages"
apt-get install ldap-auth-client nscd

echo "setup auth services to look in ldap"
auth-client-config -t nss -p lac_ldap

echo "configure to create home folder on login"
echo "\nsession required\tpam_mkhomedir.so skel=/etc/skel umask=0022\n" > /etc/pam.d/common-session

echo "assigning ldap users to local groups"
echo "TODO"

echo "restricting access from LDAP to single user xx"
echo "TODO"

echo "restarting naming service"
/etc/init.d/nscd restart

echo "finished."
