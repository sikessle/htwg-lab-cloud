#!/bin/bash

if [ "$(whoami)" != "root" ]; then
	echo "sudo/root required. Stopping"
	exit 1
fi

echo "installing cloud packages"
apt-get -y install cloud-init cloud-utils cloud-initramfs-growroot

echo "allowing password login via cloud.cfg"
sed -i 's/lock_passwd: True/lock_passwd: False/g' /etc/cloud/cloud.cfg

echo "deleting self"
rm -- "$0"

echo "shutting down"
shutdown -h now

