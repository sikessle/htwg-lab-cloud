#!/bin/bash

# Deploys feature

# Security group rules
cd ~/devstack
source openrc admin admin
nova secgroup-add-rule default tcp 22 22 0.0.0.0/0
nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
cd ..