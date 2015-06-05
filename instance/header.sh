#!/bin/sh

# 
# Before running this script, replace ##INSERT_USERNAME## through the real username.
# USE Linux tools: sed -i '' 's/##INSERT_USERNAME##/exampleuser/g' instance-setup.sh
#

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

#######################

