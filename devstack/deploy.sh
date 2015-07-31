#!/bin/bash

# Deploys devstack

sudo apt-get install -y git

./set_admin_data.sh

# install devstack
git clone https://github.com/openstack-dev/devstack.git -b stable/kilo ~/devstack/
cp "local.conf" ~/devstack/
~/devstack/stack.sh
sed -i "s/OFFLINE=False/OFFLINE=True/g" ~/devstack/local.conf 

./set_policy.sh

cd util
./ldap_init.sh
cd ..

# wait a few seconds because of possible apache restarts
sleep 10

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


# sleep 10

# ADD HERE YOUR FEATURES. DON'T FORGET TO SWITCH DIR BACK TO THIS DIR.
