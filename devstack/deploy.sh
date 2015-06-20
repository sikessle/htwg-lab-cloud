#!/bin/bash

# Deploys devstack

# setup network adapters
(
cd nova-network
./deploy.sh
)

# install devstack
git clone https://github.com/openstack-dev/devstack.git -b stable/kilo ~/devstack/
cp "local.conf" ~/devstack/
(
cd ~/devstack
./stack.sh
)
sed -i "s/OFFLINE=False/OFFLINE=True/g" ~/devstack/local.conf 

# install dashboard customizations
(
cd dashboard-theme
./deploy.sh
)
(
cd dashboard-panel-extension
./deploy.sh
)
