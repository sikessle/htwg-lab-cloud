#######################

# 
# Executed at the end of all other scripts
#

echo "------------------------------------"
echo "------------END OF SETUP------------"
echo "-----------rebooting now------------"
echo "------------------------------------"

sleep 15

# Some installation script may need a reboot (especially the ldap-login)
reboot

#######################