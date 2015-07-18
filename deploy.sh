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

# Get the IP address of the public adapter where the dashboard will be visible.
ip=$(ifconfig | grep eth2 -A 1 | grep "inet addr:[0-9|\.]*" -o | grep "[0-9|\.]*" -o)
iplength=${#ip} 
# Do some padding, to make the output look nicer :)
let padding=(17-iplength)

echo "+----------------------------+"
echo "|                            |"
echo "|  HTWG Lab Cloud installed  |"
echo "|                            |"
echo "|          Dashboard         |"
printf "|   http://$ip %${padding}s|\n"
echo "|                            |"
echo "+----------------------------+"
