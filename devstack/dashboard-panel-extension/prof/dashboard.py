from django.utils.translation import ugettext_lazy as _

import horizon


class Prof(horizon.Dashboard):
    name = _("Professor")	# Name in the navigation
    slug = "prof"		# URL
    panels = ('courses',)  	# Add the panels
    default_panel = 'courses'  	# Specify the slug of the dashboard's default panel


horizon.register(Prof)
