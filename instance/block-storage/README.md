# Mount Cinder block storage on instance

Mounts an attached block storage from Cinder as Ext4.

- Mount attached block storage, if available, as Ext4 and name it "lab-drive"
- Add directory to sidebar in nautilus

## Script notes

As the volumne (block storage) is not always available or may be available after the /etc/fstab file got processed. Therefor we have to deploy this mount strategy:

- Create mount point /media/lab-drive
- Create entry in /etc/fstab
- Create udev rule file in /etc/udev/rules.d/80-mount.rules. Here we run `mount -a` to re-process the fstab file.
- Check on each mount if the lab-drive is already formatted to ext4 and format it if necessary.

Involved files: 

- /etc/fstab Mounting parameters and correct user rights:
	``
- /etc/udev/rules.d/80-mount.rules runs as soon as the block device is available:
	`SUBSYSTEM=="block", run+="/bin/mount -a"`
- /etc/udev/rules.d/99-udisks2.rules to modify the default mount point to /media/*:
	`ENV{ID_FS_USAGE}=="filesystem|other|crypto", ENV{UDISKS_FILESYSTEM_SHARED}="1"`
