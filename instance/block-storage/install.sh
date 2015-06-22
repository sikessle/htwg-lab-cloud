# This script is only a part of the main script in the superfolder!

LAB_DRIVE_SCRIPT="/usr/local/bin/mount-lab-drive.sh"
LAB_DRIVE_MNT_POINT="/media/lab-drive"
LAB_DRIVE_MNT_FSTAB="/dev/vdb	$LAB_DRIVE_MNT_POINT	ext4	rw,suid,dev,exec,auto,users,async,nobootwait	0	0"

echo "creating mount script"

echo "#!/bin/bash" >> $LAB_DRIVE_SCRIPT
echo "# check current fstype. WARNING: MUST be running under sudo, otherwise not showing up!" >> $LAB_DRIVE_SCRIPT
echo "LAB_DRIVE_FSTYPE=\$(blkid -o value -s TYPE /dev/vdb)" >> $LAB_DRIVE_SCRIPT
echo "if [ \"\$LAB_DRIVE_FSTYPE\" != \"ext4\" ]; then" >> $LAB_DRIVE_SCRIPT
echo "	# create filesystem" >> $LAB_DRIVE_SCRIPT
echo "	mkfs.ext4 /dev/vdb" >> $LAB_DRIVE_SCRIPT
echo "fi" >> $LAB_DRIVE_SCRIPT
echo "mount -a" >> $LAB_DRIVE_SCRIPT
echo "chmod 777 $LAB_DRIVE_MNT_POINT" >> $LAB_DRIVE_SCRIPT

chmod +x $LAB_DRIVE_SCRIPT

#### end creating mount script

echo "creating mount point $LAB_DRIVE_MNT_POINT"
mkdir $LAB_DRIVE_MNT_POINT
chmod 777 $LAB_DRIVE_MNT_POINT

echo "adjusting /etc/fstab"
echo "$LAB_DRIVE_MNT_FSTAB" >> /etc/fstab
echo "" >> /etc/fstab

echo "configuring udev"
echo "SUBSYSTEM==\"block\", RUN+=\"$LAB_DRIVE_SCRIPT\"" >> /etc/udev/rules.d/80-mount.rules
echo "ENV{ID_FS_USAGE}==\"filesystem|other|crypto\", ENV{UDISKS_FILESYSTEM_SHARED}=\"1\"" >> /etc/udev/rules.d/99-udisks2.rules

echo "reload rules for udev"
udevadm control --reload-rules


echo "finished configuring lab-drive"
