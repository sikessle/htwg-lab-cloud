#!/bin/sh


if [ "$(whoami)" != "root" ]; then
	echo "root/sudo required. Stopping."
	exit 1
fi



echo "finished."
