# Extension Installation

First copy the folder named "prof" to "/opt/stack/horizon/openstack_dashboard/dashboards".

In order to make the extension show up, you need to create a file called "_50_prof.py" under "/opt/stack/horizon/openstack_dashboard/enabled" and add the following:

	# The name of the dashboard to be added to HORIZON['dashboards']. Required.
	DASHBOARD = 'prof'

	# If set to True, this dashboard will not be added to the settings.
	DISABLED = False

	# A list of applications to be added to INSTALLED_APPS.
	ADD_INSTALLED_APPS = [
    'openstack_dashboard.prof.courses',
	]

Now, restart the web server:

	sudo service apache2 restart

# Using the extension

View the extension in your dashboard at the url:

	http://yourHost/prof/
