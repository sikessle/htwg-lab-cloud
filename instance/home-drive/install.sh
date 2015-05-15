#!/bin/sh

# First argument $1 must be the username (uid)

if [ "$(whoami)" != "root" ]; then
	echo "root/sudo required. Stopping."
	exit 1
fi

USER=$1


