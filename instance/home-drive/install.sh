# This script is only a part of a the main script in the superfolder!

MNT_POINT=/mnt/home-drive
PAM_GLOBAL_CONF=/etc/security/pam_mount.conf.xml

echo "installing required packages"
apt-get install -y libpam-mount cifs-utils

echo "configuring auto-mounting of home-drive"
mkdir $MNT_POINT

echo "" > $PAM_GLOBAL_CONF
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
