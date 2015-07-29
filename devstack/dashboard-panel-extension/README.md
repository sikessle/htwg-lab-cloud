# Deployment

Horizon must be installed.

First execute the deploy script **deploy.sh** to setup the dashboard extension.

The deploy script will copy the extension folder to horizon. The script will
also copy a file for the setup of an instance. For more information check out
the deploy script.

In order to make the extension show up the deploy script will create a file called  **_50_prof.py** under **/opt/stack/horizon/openstack_dashboard/enabled** with the following content:

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

At the end the deploy script will restart horizon:
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

# Uploading an Image
Horizon provide some default images which can be used. To use our own image we
need to upload one.
We could upload the image from the **instance** folder from the root directory of this project.
Therefore download the image as described in the **instance** README and execute the
commands from below. Note that the tenant if should be replaced by a valid tenant id.
```
export OS_USERNAME=admin
export OS_PASSWORD=adminpw
export OS_TENANT_ID=1
export OS_AUTH_URL="http://192.168.35.128:35357/v2.0"
glance image-create --name='base' --is-public=true --container-format=bare --disk-format=qcow2 < ubuntu-14.04-openstack-qcow2.img
```
