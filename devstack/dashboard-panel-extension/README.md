# Deployment

Horizon must be installed.

First copy the folder named **prof** to **opt/stack/horizon/openstack_dashboard/dashboards**.

In order to make the extension show up, you need to create a file called **_50_prof.py** under **/opt/stack/horizon/openstack_dashboard/enabled** and add the following:

```python
# The name of the dashboard to be added to HORIZON['dashboards']. Required.
DASHBOARD = 'prof'

# If set to True, this dashboard will not be added to the settings.
DISABLED = False

# A list of applications to be added to INSTALLED_APPS.
ADD_INSTALLED_APPS = [
	'openstack_dashboard.dashboards.prof',
]
```

Now stop and restart the web server:
```
sudo service apache2 stop
sudo service apache2 restart
```

# Using the extension

View the extension in your dashboard at the url:
```
http://yourHost/prof/
```

# Mail support
If you start instances for a course, the HTWG Cloud will send an email to each member
of that course.
This email contain the link to access the virtual machine.

To configure the email host, go to **/opt/stack/horizon/openstack_dashboard/local/local_settings.py**

There you can configure an outgoing email host with SMTP or redirect emails to a file (for test purpose).
To find the configuration section, search for **EMAIL_BACKEND** in **local_settings.py**

Note : **local_settings.py** will be overwritten if you execute stack.sh

If you like to use another EMAIL_BACKEND do these steps
- ./stack.sh
- sudo service apache2 stop
- modify local_settings.py
- sudo service apache2 restart

To write each send mail to a file use for example this configuration

	EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
	EMAIL_FILE_PATH = '/tmp/app-messages'

Each message will now be stored in a file which is located in the above folder.

Fore more information about possible configurations [this](https://docs.djangoproject.com/en/1.8/topics/email/) link might be helpful.
