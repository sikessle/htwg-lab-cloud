#!/bin/sh

# 
# Before running this script, replace ##INSERT_USERNAME## through the real username.
#

USER="##INSERT_USERNAME##"

if [ "$USER" == "##INSERT_USERNAME##" ]; then
	echo "##INSERT_USERNAME## not replaced by real username. Stopping."
	exit 1
fi

if [ "$(whoami)" != "root" ]; then
	echo "root/sudo required. Stopping."
	exit 1
fi

MNT_POINT=/mnt/home-drive
PAM_LOCAL_CONF=/home/$USER/.pam_mount.conf.xml
PAM_GLOBAL_CONF=/etc/security/pam_mount.conf.xml

echo "installing required packages"
apt-get install -y libpam_mount cifs-utils

echo "configuing auto-mounting of home-drive"
mkdir $MNT_POINT
touch $PAM_LOCAL_CONF

echo "<?xml version=\"1.0\" encoding=\"utf-8\" ?>" >> $PAM_LOCAL_CONF
echo "<!DOCTYPE pam_mount SYSTEM \"pam_mount.conf.xml.dtd\">" >> $PAM_LOCAL_CONF
echo "<pam_mount>" >> $PAM_LOCAL_CONF
echo "<volume options=\"user=$USER,workgroup=FHKN,domain=FHKN\" user=\"$USER\" mountpoint=\"/media/home-drive\" path=\"//homedrive.htwg-konstanz.de/home\" fstype=\"cifs\" />" >> $PAM_LOCAL_CONF
echo "</pam_mount>" >> $PAM_LOCAL_CONF

echo "<?xml version=\"1.0\" encoding=\"utf-8\" ?>" >> $PAM_GLOBAL_CONF
echo "<!DOCTYPE pam_mount SYSTEM \"pam_mount.conf.xml.dtd\">" >> $PAM_GLOBAL_CONF
echo "<pam_mount>" >> $PAM_GLOBAL_CONF
echo "<debug enable=\"0\" />" >> $PAM_GLOBAL_CONF
echo "<luserconf name=\".pam_mount.conf.xml\" />" >> $PAM_GLOBAL_CONF
echo "<mntoptions require=\"\" />" >> $PAM_GLOBAL_CONF
echo "<mntoptions allow=\"*\" />" >> $PAM_GLOBAL_CONF
echo "<!-- mntoptions deny=\"suid,dev\" / -->" >> $PAM_GLOBAL_CONF
echo "<!-- mntoptions require=\"nosuid,nodev\" / -->" >> $PAM_GLOBAL_CONF
echo "<path>/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin</path>" >> $PAM_GLOBAL_CONF
echo "<logout wait=\"0\" hup=\"0\" term=\"0\" kill=\"0\" />" >> $PAM_GLOBAL_CONF
echo "<mkmountpoint enable=\"1\" remove=\"true\" />" >> $PAM_GLOBAL_CONF
echo "</pam_mount>" >> $PAM_GLOBAL_CONF
