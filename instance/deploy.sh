#!/bin/bash

# Deploys the instance script to /opt/stack/htwg/instance-setup.sh

# Because of the file size, the image is hosted on Dropbox.
IMAGE_DL="https://www.dropbox.com/sh/0dgcaxc2u7cbfgi/AABhaR7-cTC_JcWDwWAtloO3a/ubuntu-14.04-openstack-qcow2.img?dl=1"

make
mkdir /opt/stack/htwg
cp instance-setup.sh /opt/stack/htwg/

# Disabled for faster testing. If you want a self-contained productivity system, 
# uncomment the line below.
echo "Uncomment to enable image download"
#wget -O ~/ubuntu-14.04-openstack-qcow2.img "$IMAGE_DL"
