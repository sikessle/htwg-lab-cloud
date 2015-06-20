#!/bin/bash

# Deploys devstack

# setup network adapters
nova-network/deploy.sh

# install devstack
git clone https://github.com/openstack-dev/devstack.git -b stable/kilo ~/devstack/
cp "local.conf" ~/devstack/
~/devstack/stack.sh
sed -i "s/OFFLINE=False/OFFLINE=True/g" ~/devstack/local.conf 

# install dashboard customizations
dashboard-theme/deploy.sh
dashboard-panel-extension/deploy.sh

