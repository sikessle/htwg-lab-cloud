#######################

# 
# Executed at the end of all other scripts
#

if [ "$(whoami)" != "root" ]; then
	echo "root/sudo required. Stopping."
	exit 1
fi

reboot

#######################