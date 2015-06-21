#!/bin/bash

# Deploys the HTWG Lab Cloud

if [ "$(whoami)" == "root" ]; then
	echo "Required to run as normal user. Stopping."
	exit 1
fi

cd devstack
./deploy.sh || echo "failed. Stopping."
cd ..

cd instance
./deploy.sh || echo "failed. Stopping."
cd ..

ip=$(ifconfig | grep eth2 -A 1 | grep "inet addr:[0-9|\.]*" -o | grep "[0-9|\.]*" -o)

echo "+----------------------------+"
echo "|                            |"
echo "|  HTWG Lab Cloud installed  |"
echo "|                            |"
echo "|          Dashboard         |"
echo "     http://$ip      			"
echo "|                            |"
echo "+----------------------------+"
