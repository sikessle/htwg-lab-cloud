#!/bin/bash

# Deploys this feature

echo "CUSTOM_THEME_PATH = 'static/themes/lab-cloud'" >> /opt/stack/horizon/openstack_dashboard/local/local_settings.py
# add HTWG Lab Cloud to the browser's title bar
echo "SITE_BRANDING = 'HTWG Lab Cloud'" >> /opt/stack/horizon/openstack_dashboard/local/local_settings.py

# Copy files to the themes folder and run some manage.py scripts to re-compile
cp -r lab-cloud /opt/stack/horizon/openstack_dashboard/static/themes/
python /opt/stack/horizon/manage.py collectstatic --noinput --clear
python /opt/stack/horizon/manage.py compress --force
sleep 3

sudo service apache2 restart
