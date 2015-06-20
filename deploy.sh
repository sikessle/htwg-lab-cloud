#!/bin/bash

# Deploys the HTWG Lab Cloud

if [ "$(whoami)" == "root" ]; then
	echo "Required to run as normal user. Stopping."
	exit 1
fi

sudo apt-get install -y git
sudo apt-get install -y make

(
cd devstack
./deploy.sh
) || (echo "failed. Stopping." && exit 1)
(
cd instance
./deploy.sh
) || (echo "failed. Stopping." && exit 1)

echo "**********************************"
echo "HTWG Lab Cloud installed."
echo "**********************************"
