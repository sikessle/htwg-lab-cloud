#!/bin/sh

# 
# Before running this script, replace ##INSERT_USERNAME## through the real username.
#

USER="##INSERT_USERNAME##"

if [ "$USER" = "##INSERT_USERNAME##" ]; then
	echo "##INSERT_USERNAME## not replaced by real username. Stopping."
	exit 1
fi

if [ "$(whoami)" != "root" ]; then
	echo "root/sudo required. Stopping."
	exit 1
fi


#######################

