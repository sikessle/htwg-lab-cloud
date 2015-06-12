# This script is only a part of the main script in the superfolder!

LAB_DRIVE_MNT_POINT="/media/lab-drive"
LAB_DRIVE_MNT_FSTAB="/dev/vdb\t$LAB_DRIVE_MNT_POINT\text4\trw,suid,dev,exec,auto,users,async\t0\t0"

echo "creating mount point $LAB_DRIVE_MNT_POINT"
mkdir $LAB_DRIVE_MNT_POINT
chmod 777 $LAB_DRIVE_MNT_POINT

echo "adjusting /etc/fstab"
echo "$LAB_DRIVE_MNT_FSTAB\n" >> /etc/fstab

echo "configuring udev"
echo "SUBSYSTEM==\"block\", RUN+=\"/bin/mount -a\"\n" >> /etc/udev/rules.d/80-mount.rules
echo "ENV{ID_FS_USAGE}==\"filesystem|other|crypto\", ENV{UDISKS_FILESYSTEM_SHARED}=\"1\"\n" >> /etc/udev/rules.d/99-udisks2.rules

echo "re-mounting to check if lab-drive is already available"
mount -a
udevadm control --reload-rules

echo "finished configuring lab-drive"
