#!/bin/bash

# Deploys this feature

# copy the instance init script
cp ../../instance/instance-setup.sh prof/courses
# copy the dashboard extension
cp -r prof /opt/stack/horizon/openstack_dashboard/dashboards/
# copy the file to enable the dashboard extension
cp "_50_prof.py" /opt/stack/horizon/openstack_dashboard/enabled/
sleep 3
sudo service apache2 restart
