# This script is only a part of the main script in the superfolder!

# Mount at /media -> this enables the entry in the sidebar of nautilus automatically. 
HOME_MNT_POINT="/media/home-drive"
# Global config file of PAM-Mount. We stuff all configuration in this files, as
# only a single user is owner of the machine. So no need for multiple user-specific configs.
PAM_GLOBAL_CONF="/etc/security/pam_mount.conf.xml"

echo "installing required packages"
apt-get install -y libpam-mount cifs-utils

echo "configuring auto-mounting of home-drive"
mkdir $HOME_MNT_POINT

sleep 2

# Delete if it exists to start with a fresh copy
rm -f $PAM_GLOBAL_CONF

sleep 2
# Setting the required config options in the XML file
echo "<?xml version=\"1.0\" encoding=\"utf-8\" ?>" >> $PAM_GLOBAL_CONF
echo "<!DOCTYPE pam_mount SYSTEM \"pam_mount.conf.xml.dtd\">" >> $PAM_GLOBAL_CONF
echo "<pam_mount>" >> $PAM_GLOBAL_CONF
echo "<debug enable=\"0\" />" >> $PAM_GLOBAL_CONF
# This line is important. It sets the volumne mount options.
echo "<volume options=\"user=$USER,workgroup=FHKN,domain=FHKN\" user=\"$USER\" mountpoint=\"$HOME_MNT_POINT\" path=\"//homedrive.htwg-konstanz.de/home\" fstype=\"cifs\" />" >> $PAM_GLOBAL_CONF
echo "<mntoptions require=\"\" />" >> $PAM_GLOBAL_CONF
echo "<mntoptions allow=\"*\" />" >> $PAM_GLOBAL_CONF
echo "<!-- mntoptions deny=\"suid,dev\" / -->" >> $PAM_GLOBAL_CONF
echo "<!-- mntoptions require=\"nosuid,nodev\" / -->" >> $PAM_GLOBAL_CONF
echo "<path>/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin</path>" >> $PAM_GLOBAL_CONF
echo "<logout wait=\"0\" hup=\"0\" term=\"0\" kill=\"0\" />" >> $PAM_GLOBAL_CONF
echo "<mkmountpoint enable=\"1\" remove=\"true\" />" >> $PAM_GLOBAL_CONF
echo "</pam_mount>" >> $PAM_GLOBAL_CONF
