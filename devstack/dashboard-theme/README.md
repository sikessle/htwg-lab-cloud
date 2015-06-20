# A Theme for the Dashboard in HTWG Style

## Requirements

- OpenStack `kilo` Release

## Deployment

Horizon must be installed. Then:

- Add `CUSTOM_THEME_PATH = 'static/themes/lab-cloud'` and `SITE_BRANDING = 'HTWG Lab Cloud'` to `horizon/openstack_dashboard/local/local_settings.py`
- Copy `lab-cloud` to `horizon/openstack_dashboard/static/themes/`
- Run in `horizon/` folder `python manage.py collectstatic --noinput --clear`
- Run in `horizon/` folder `python manage.py compress --force`
- Restart web server with `sudo service apache2 restart`
