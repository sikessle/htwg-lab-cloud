#!/bin/bash

# Deploys feature

# Security group rules
cwd=$(pwd)
cd ~/devstack
source openrc admin admin
nova secgroup-add-rule default tcp -1 -1 0.0.0.0/0
nova secgroup-add-rule default udp -1 -1 0.0.0.0/0
nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
cd cwd