#!/bin/bash

# Deploys this feature

# Disabling network manager
sudo stop network-manager
echo "manual" | sudo tee /etc/init/network-manager.override

sudo cp interfaces.txt /etc/network/interfaces
sudo ifdown --exclude=lo -a && sudo ifup --exclude=lo -a
