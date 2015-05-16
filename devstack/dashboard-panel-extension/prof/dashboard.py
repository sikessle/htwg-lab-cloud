from django.utils.translation import ugettext_lazy as _

import horizon


class Prof(horizon.Dashboard):
    name = _("Prof")
    slug = "prof"
    panels = ('courses',)  # Add your panels here.
    default_panel = 'courses'  # Specify the slug of the dashboard's default panel.


horizon.register(Prof)
