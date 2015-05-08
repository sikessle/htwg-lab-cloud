#!/bin/sh

# First argument $1 must be the username (uid)

if [ "$(whoami)" != "root" ]; then
	echo "root/sudo required. Stopping."
	exit 1
fi

USER=$1

echo "configuring ldap for user $USER"

echo "installing ldap packages"
DEBIAN_FRONTEND=noninteractive apt-get -y -q install ldap-auth-client nscd

echo "configuring ldap config files"
echo "base ou=users,dc=fh-konstanz,dc=de\nuri ldap://ldap.htwg-konstanz.de/\nldap_version 3\npam_password md5\nnss_override_attribute_value homeDirectory /home/$USER\nnss_override_attribute_value gidNumber 2000\nnss_override_attribute_value uidNumber 2000\nnss_override_attribute_value loginShell /bin/bash\n" > /etc/ldap.conf

echo "setup auth services to look in ldap"
auth-client-config -t nss -p lac_ldap

echo "configure to create home folder on login"
echo "\nsession required\tpam_mkhomedir.so skel=/etc/skel umask=0022\n" > /etc/pam.d/common-session

echo "assigning ldap users to local groups"
echo "\n*;*;*;Al0000-2400;adm,cdrom,sudo,dip,plugdev,lpadmin,sambashare\n" >> /etc/security/group.conf 
echo "\n\nauth\trequired\tpam_group.so use_first_pass\n" >> /etc/pam.d/common-auth
echo "\n$USER:x:2000:\n" >> /etc/group


echo "restricting access from LDAP to single user $USER"
echo "\nnss_base_passwd uid=$USER,ou=users,dc=fh-konstanz,dc=de\n" >> /etc/ldap.conf

echo "restarting naming service"
/etc/init.d/nscd restart

echo "finished."
