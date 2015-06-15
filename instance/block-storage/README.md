# Mount Cinder block storage on instance

Mounts an attached block storage from Cinder as Ext4.

- Mount attached block storage, if available, as Ext4 and name it "lab-drive"
- Add directory to sidebar in nautilus

## Requirements

The `lab-drive` must be the **first** attached volume, as it is assumed to be mapped under /dev/vdb.

## Script notes

As the volumne (block storage) is not always available or may be available after the /etc/fstab file got processed. The drive will be formatted as ext4. Therefore we have to deploy this mount strategy:

- Create mount point /media/lab-drive
- Create entry in /etc/fstab
- Create udev rule file in /etc/udev/rules.d/80-mount.rules. Here we run `mount -a` to re-process the fstab file.

Involved files: 

- /etc/fstab Mounting parameters and correct user rights.
- /etc/udev/rules.d/80-mount.rules runs as soon as the block device is available.
- /etc/udev/rules.d/99-udisks2.rules to modify the default mount point to /media/*
- /usr/local/bin/mount-lab-drive.sh to mount and format the drive. Will be called from the 80-mount.rules udev rule.
