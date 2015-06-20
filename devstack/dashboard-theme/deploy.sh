#!/bin/bash

# Deploys this feature

cp local_settings.py horizon/openstack_dashboard/local/
cp lab-cloud /opt/stack/horizon/openstack_dashboard/static/themes/
python /opt/stack/horizon/manage.py collectstatic --noinput --clear
python /opt/stack/horizon/manage.py compress --force
sudo service apache2 restart
