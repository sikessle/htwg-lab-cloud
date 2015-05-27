from django.utils.translation import ugettext_lazy as _

from horizon import tables

# action to start instances
class StartInstancesAction(tables.LinkAction):
    name = "start instance"
    verbose_name = _("Start Instances")
    url = "horizon:prof:courses:start_instances"
    classes = ("ajax-modal",)

    def allowed(self, request, instance=None):
        return True

# default row filter
class FilterAction(tables.FilterAction):
    name = "filter"

class CoursesTable(tables.DataTable):
    name = tables.Column('name', \
                         verbose_name=_("Name"))
    description = tables.Column('description', \
                           verbose_name=_("Description"))
    id = tables.Column('id', \
                         verbose_name=_("ID"))
    enabled = tables.Column('enabled', \
                               verbose_name=_("Enabled"))

    class Meta:
        name = "coursesTbl"
        verbose_name = _("Courses")
	table_actions = (FilterAction,)
	row_actions = (StartInstancesAction,)
