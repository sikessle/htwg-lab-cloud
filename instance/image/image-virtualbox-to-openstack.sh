#!/bin/bash

IMAGE=$1
TARGET="ubuntu-14.04-openstack"

if [ "$IMAGE" = "" ]; then
	echo "pass as first argument the *FULL* path to the image you want to convert"
	exit 1
fi

IMAGE="/Users/sikessle/Documents/Software/Virtual Machines/OpenStack/Cloud-Image Ubuntu/Cloud-Image Ubuntu.vdi"

echo "converting $IMAGE to openstack compatible format"

VBoxManage clonehd "$IMAGE" $TARGET-raw.img --format raw
qemu-img convert -f raw -O qcow2 "${TARGET}-raw.img" "${TARGET}-qcow2.img"
rm -f "${TARGET}-raw.img"