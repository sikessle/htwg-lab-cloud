#!/bin/bash

# Deploys the HTWG Lab Cloud

if [ "$(whoami)" == "root" ]; then
	echo "Required to run as normal user. Stopping."
	exit 1
fi

devstack/deploy.sh || (echo "failed. Stopping." && exit 1)
instance/deploy.sh || (echo "failed. Stopping." && exit 1)

echo "**********************************"
echo "HTWG Lab Cloud installed."
echo "**********************************"