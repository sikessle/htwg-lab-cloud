# This script is only a part of the main script in the superfolder!

# Script which handles the formatting and mounting of the block storage drive.
LAB_DRIVE_SCRIPT="/usr/local/bin/mount-lab-drive.sh"
# Mount at /media to enable Nautilus to show the folder in the sidebar automatically.
LAB_DRIVE_MNT_POINT="/media/lab-drive"
# Mount line in the fstab file.
LAB_DRIVE_MNT_FSTAB="/dev/vdb	$LAB_DRIVE_MNT_POINT	ext4	rw,suid,dev,exec,auto,users,async,nobootwait	0	0"

echo "creating mount script"

# This script checks if the lab-drive is mounted for the first time and if so, then formats it
# as ext4. Otherwise it is just mounted.
echo "#!/bin/bash" >> $LAB_DRIVE_SCRIPT
echo "# check current fstype. WARNING: MUST be running under sudo, otherwise not showing up!" >> $LAB_DRIVE_SCRIPT
echo "LAB_DRIVE_FSTYPE=\$(blkid -o value -s TYPE /dev/vdb)" >> $LAB_DRIVE_SCRIPT
echo "if [ \"\$LAB_DRIVE_FSTYPE\" != \"ext4\" ]; then" >> $LAB_DRIVE_SCRIPT
echo "	# create filesystem" >> $LAB_DRIVE_SCRIPT
echo "	mkfs.ext4 /dev/vdb" >> $LAB_DRIVE_SCRIPT
echo "fi" >> $LAB_DRIVE_SCRIPT
echo "mount -a" >> $LAB_DRIVE_SCRIPT
echo "chmod 777 $LAB_DRIVE_MNT_POINT" >> $LAB_DRIVE_SCRIPT

# Script must executable
chmod +x $LAB_DRIVE_SCRIPT

#### end creating mount script


echo "creating mount point $LAB_DRIVE_MNT_POINT"
mkdir $LAB_DRIVE_MNT_POINT
chmod 777 $LAB_DRIVE_MNT_POINT

echo "adjusting /etc/fstab"
echo "$LAB_DRIVE_MNT_FSTAB" >> /etc/fstab
echo "" >> /etc/fstab

echo "configuring udev"
# Setting up udev to run our mount script every time the linux block-subsystem has detected a change.
echo "SUBSYSTEM==\"block\", RUN+=\"$LAB_DRIVE_SCRIPT\"" >> /etc/udev/rules.d/80-mount.rules
echo "ENV{ID_FS_USAGE}==\"filesystem|other|crypto\", ENV{UDISKS_FILESYSTEM_SHARED}=\"1\"" >> /etc/udev/rules.d/99-udisks2.rules

echo "reload rules for udev"
udevadm control --reload-rules


echo "finished configuring lab-drive"
