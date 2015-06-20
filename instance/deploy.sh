#!/bin/bash

# Deploys the instance script

IMAGE_DL="https://www.dropbox.com/sh/0dgcaxc2u7cbfgi/AABhaR7-cTC_JcWDwWAtloO3a/ubuntu-14.04-openstack-qcow2.img?dl=1"

make
echo "TODO: Where must this script be copied to?"
cp instance-setup.sh ~/

echo "Uncomment to enable image download"
#wget -O ~/ubuntu-14.04-openstack-qcow2.img "$IMAGE_DL"