#!/bin/bash

# 
# Before running this script, replace ##INSERT_USERNAME## through the real username.
# USE Linux tools: sed -i '' 's/##INSERT_USERNAME##/exampleuser/g' instance-setup.sh
#

echo "------------------------------------"
echo "----------START OF SETUP------------"
echo "------------------------------------"

USER="##INSERT_USERNAME##"

if [ "${USER:0:2}" == "##" ]; then
	echo "username placeholder not replaced by real username. Stopping."
	exit 1
fi

if [ "$(whoami)" != "root" ]; then
	echo "root/sudo required. Stopping."
	exit 1
fi


echo "updating apt-get"
apt-get update 
# give some cooldown time because of locks
# especially in slow qemu environment
sleep 15

#######################

