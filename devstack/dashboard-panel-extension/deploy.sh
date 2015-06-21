#!/bin/bash

# Deploys this feature
sudo service apache2 stop
cp -r prof /opt/stack/horizon/openstack_dashboard/dashboards/
cp "_50_prof.py" /opt/stack/horizon/openstack_dashboard/enabled/
sudo service apache2 restart
