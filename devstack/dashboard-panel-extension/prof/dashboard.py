from django.utils.translation import ugettext_lazy as _

import horizon


class Prof(horizon.Dashboard):
    name = _("Professor")	# name in the navigation
    slug = "prof"		# url
    panels = ('courses',)  	# Add your panels here.
    default_panel = 'courses'  	# Specify the slug of the dashboard's default panel.


horizon.register(Prof)
