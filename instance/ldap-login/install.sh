# This script is only a part of the main script in the superfolder!

# Distinguished name of the users at the HTWG LDAP
BASEDN="ou=users,dc=fh-konstanz,dc=de"
LDAP_CONF="/etc/ldap.conf"
LDM_CONF="/etc/lightdm/lightdm.conf"

echo "configuring ldap for user: $USER"

echo "installing ldap packages"
# Using noninteractive mode to suppress dialogs as we are running unattended.
DEBIAN_FRONTEND=noninteractive apt-get -y -q install ldap-auth-client nscd

echo "configuring ldap config files"
echo "" > $LDAP_CONF
echo "base $BASEDN" >> $LDAP_CONF
# The HTWG LDAP Server URL
echo "uri ldap://ldap.htwg-konstanz.de/" >> $LDAP_CONF
echo "ldap_version 3" >> $LDAP_CONF
echo "pam_password md5" >> $LDAP_CONF
# Overriding invalid values from the LDAP to match our local machine.
echo "nss_override_attribute_value homeDirectory /home/$USER" >> $LDAP_CONF
echo "nss_override_attribute_value gidNumber 2000" >> $LDAP_CONF
echo "nss_override_attribute_value uidNumber 2000" >> $LDAP_CONF
echo "nss_override_attribute_value loginShell /bin/bash" >> $LDAP_CONF

# Only a single user is allowed to access this machine, so add a filter on the LDAP users.
echo "restricting access from LDAP to single user: $USER"
echo "nss_base_passwd uid=$USER,$BASEDN" >> $LDAP_CONF

echo "setup auth services to look in ldap"
auth-client-config -t nss -p lac_ldap

echo "configure to create home folder on login"
echo "" >> /etc/pam.d/common-session
echo "session required	pam_mkhomedir.so skel=/etc/skel umask=0022" >> /etc/pam.d/common-session

echo "assigning ldap users to local groups"
echo "" >> /etc/security/group.conf 
# Default groups..
echo "*;*;*;Al0000-2400;adm,cdrom,sudo,dip,plugdev,lpadmin,sambashare" >> /etc/security/group.conf 
echo "" >> /etc/pam.d/common-auth
echo "auth 	required 	pam_group.so use_first_pass" >> /etc/pam.d/common-auth
echo "" >> /etc/group
echo "$USER:x:2000:" >> /etc/group

echo "configuring graphical login (greeter)"
rm -f $LDM_CONF
echo "[SeatDefaults]" >> $LDM_CONF
# We must show the manual login, so users can enter their username as on first login it 
# is not yet contained in the user list.
echo "greeter-show-manual-login=true" >> $LDM_CONF
echo "allow-guest=false" >> $LDM_CONF
echo "user-session=ubuntu" >> $LDM_CONF

echo "restarting naming service"
/etc/init.d/nscd restart

echo "finished."
