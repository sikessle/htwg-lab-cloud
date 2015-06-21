#!/bin/bash

# Deploys devstack

# install devstack
git clone https://github.com/openstack-dev/devstack.git -b stable/kilo ~/devstack/
cp "local.conf" ~/devstack/
~/devstack/stack.sh
sed -i "s/OFFLINE=False/OFFLINE=True/g" ~/devstack/local.conf 

cd network
./deploy.sh
cd ..

# wait a few seconds because of possible apache restarts
sleep 10

# install dashboard customizations
cd dashboard-theme
./deploy.sh
cd ..

# wait a few seconds because of possible apache restarts
sleep 10

cd dashboard-panel-extension
./deploy.sh
cd ..
