#!/bin/bash

IMAGE=$1
TARGET="ubuntu-14.04-openstack"

if [ "$IMAGE" = "" ]; then
	echo "pass as first argument the *FULL* path to the snapshot of the image you want to convert"
	exit 1
fi

#IMAGE="/Users/sikessle/Documents/Software/Virtual Machines/OpenStack/Cloud-Image Ubuntu/Snapshots/{b947cd20-24d0-4b1c-9779-66f7de73835a}.vdi"

echo "***************************************************"
echo "converting $IMAGE to openstack compatible format"
echo "***************************************************"

VBoxManage clonehd "$IMAGE" $TARGET-raw.img --format raw
qemu-img convert -f raw -O qcow2 "${TARGET}-raw.img" "${TARGET}-qcow2.img"
rm -f "${TARGET}-raw.img"
echo "***************************************************"
echo "${TARGET}-qcow2.img is ready to deploy in OpenStack"
echo "***************************************************"