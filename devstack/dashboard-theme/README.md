# A Theme for the Dashboard in HTWG Style

## Requirements

- OpenStack `kilo` Release

## Deployment

Horizon must be installed. Then:

- Copy `local_settings.py` to `horizon/openstack_dashboard/local/`
- Copy `lab-cloud` to `horizon/openstack_dashboard/static/themes/`
- Run in `horizon/` folder `python manage.py collectstatic --noinput --clear`
- Run in `horizon/` folder `python manage.py compress --force`
- Restart web server with `sudo service apache2 restart`
