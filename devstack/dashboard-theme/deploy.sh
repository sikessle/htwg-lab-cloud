#!/bin/bash

# Deploys this feature

echo "CUSTOM_THEME_PATH = 'static/themes/lab-cloud'" >> /opt/stack/horizon/openstack_dashboard/local/local_settings.py
echo "SITE_BRANDING = 'HTWG Lab Cloud'" >> /opt/stack/horizon/openstack_dashboard/local/local_settings.py

cp -r lab-cloud /opt/stack/horizon/openstack_dashboard/static/themes/
python /opt/stack/horizon/manage.py collectstatic --noinput --clear
python /opt/stack/horizon/manage.py compress --force
sudo service apache2 restart
