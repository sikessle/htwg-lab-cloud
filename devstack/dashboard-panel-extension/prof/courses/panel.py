from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.prof import dashboard

class Courses(horizon.Panel):
    name = _("Courses")
    slug = "courses"


dashboard.Prof.register(Courses)
