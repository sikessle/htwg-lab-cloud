# Mount Cinder block storage on instance

Mounts an attached block storage from Cinder as Ext4.

- Mount attached block storage, if available, as Ext4 and name it "lab-drive"
- Add directory to sidebar in nautilus

## Script notes

As the volumne (block storage) is not always available or may be available after the /etc/fstab file got processed. Therefor we have to deploy this mount strategy:

- Create entry in /etc/fstab
- Create udev rule file in /etc/udev/rules.d/80-mount.rules. Here we run `mount -a` to re-process the fstab file.

Involved files: 

- /etc/fstab Mounting parameters and correct user rights
- /etc/udev/rules.d/80-mount.rules runs as soon as the block device is available. 
- /etc/udev/rules.d/99-udisks2.rules to modify the default mount point to /media/*
