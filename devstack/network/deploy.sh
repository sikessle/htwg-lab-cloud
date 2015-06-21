#!/bin/bash

# Deploys feature

# Security group rules
cwd=$(pwd)
cd ~/devstack
source openrc admin admin
nova secgroup-add-rule default tcp 1 65535 0.0.0.0/0
nova secgroup-add-rule default udp 1 65535 0.0.0.0/0
nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
cd $cwd

# Enable internet in instances. 
# SNAT: sending outgoing traffic over eth0 just before it is sended.
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
