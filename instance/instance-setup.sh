#!/bin/sh

# 
# Before running this script, replace sikessle through the real username.
# USE Linux tools: sed -i '' 's/sikessle/exampleuser/g' instance-setup.sh
#

USER="sikessle"

if [ "${USER:0:2}" == "##" ]; then
	echo "username placeholder not replaced by real username. Stopping."
	exit 1
fi

if [ "$(whoami)" != "root" ]; then
	echo "root/sudo required. Stopping."
	exit 1
fi


echo "updating apt-get"
apt-get update 

#######################

# This script is only a part of a the main script in the superfolder!

BASEDN="ou=users,dc=fh-konstanz,dc=de"
LDAP_CONF=/etc/ldap.conf
LDM_CONF=/etc/lightdm/lightdm.conf

echo "configuring ldap for user: $USER"

echo "installing ldap packages"
DEBIAN_FRONTEND=noninteractive apt-get -y -q install ldap-auth-client nscd

echo "configuring ldap config files"
echo "" > $LDAP_CONF
echo "base $BASEDN" >> $LDAP_CONF
echo "uri ldap://ldap.htwg-konstanz.de/" >> $LDAP_CONF
echo "ldap_version 3" >> $LDAP_CONF
echo "pam_password md5" >> $LDAP_CONF
echo "nss_override_attribute_value homeDirectory /home/$USER" >> $LDAP_CONF
echo "nss_override_attribute_value gidNumber 2000" >> $LDAP_CONF
echo "nss_override_attribute_value uidNumber 2000" >> $LDAP_CONF
echo "nss_override_attribute_value loginShell /bin/bash" >> $LDAP_CONF

echo "restricting access from LDAP to single user: $USER"
echo "nss_base_passwd uid=$USER,$BASEDN" >> $LDAP_CONF

echo "setup auth services to look in ldap"
auth-client-config -t nss -p lac_ldap

echo "configure to create home folder on login"
echo "\nsession required\tpam_mkhomedir.so skel=/etc/skel umask=0022" >> /etc/pam.d/common-session

echo "assigning ldap users to local groups"
echo "\n*;*;*;Al0000-2400;adm,cdrom,sudo,dip,plugdev,lpadmin,sambashare" >> /etc/security/group.conf 
echo "\n\nauth\trequired\tpam_group.so use_first_pass" >> /etc/pam.d/common-auth
echo "\n$USER:x:2000:" >> /etc/group

echo "configuring graphical login (greeter)"
rm -f $LDM_CONF
echo "[SeatDefaults]" >> $LDM_CONF
echo "greeter-show-manual-login=true" >> $LDM_CONF
echo "greeter-hide-users=true" >> $LDM_CONF
echo "allow-guest=false" >> $LDM_CONF
echo "user-session=ubuntu" >> $LDM_CONF

echo "restarting naming service"
/etc/init.d/nscd restart

echo "finished."
# This script is only a part of a the main script in the superfolder!

MNT_POINT=/media/home-drive
PAM_GLOBAL_CONF=/etc/security/pam_mount.conf.xml

echo "installing required packages"
apt-get install -y libpam-mount cifs-utils

echo "configuring auto-mounting of home-drive"
mkdir $MNT_POINT

rm -f $PAM_GLOBAL_CONF
echo "<?xml version=\"1.0\" encoding=\"utf-8\" ?>" >> $PAM_GLOBAL_CONF
echo "<!DOCTYPE pam_mount SYSTEM \"pam_mount.conf.xml.dtd\">" >> $PAM_GLOBAL_CONF
echo "<pam_mount>" >> $PAM_GLOBAL_CONF
echo "<debug enable=\"0\" />" >> $PAM_GLOBAL_CONF
echo "<volume options=\"user=$USER,workgroup=FHKN,domain=FHKN\" user=\"$USER\" mountpoint=\"$MNT_POINT\" path=\"//homedrive.htwg-konstanz.de/home\" fstype=\"cifs\" />" >> $PAM_GLOBAL_CONF
echo "<mntoptions require=\"\" />" >> $PAM_GLOBAL_CONF
echo "<mntoptions allow=\"*\" />" >> $PAM_GLOBAL_CONF
echo "<!-- mntoptions deny=\"suid,dev\" / -->" >> $PAM_GLOBAL_CONF
echo "<!-- mntoptions require=\"nosuid,nodev\" / -->" >> $PAM_GLOBAL_CONF
echo "<path>/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin</path>" >> $PAM_GLOBAL_CONF
echo "<logout wait=\"0\" hup=\"0\" term=\"0\" kill=\"0\" />" >> $PAM_GLOBAL_CONF
echo "<mkmountpoint enable=\"1\" remove=\"true\" />" >> $PAM_GLOBAL_CONF
echo "</pam_mount>" >> $PAM_GLOBAL_CONF
# This script is only a part of a the main script in the superfolder!

#######################

# 
# Executed at the end of all other scripts
#

reboot

#######################
