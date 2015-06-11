from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables

from .course import Course
from .course import CourseHelper

# action to start instances
class StartInstancesAction(tables.LinkAction):
    name = "start instance"
    verbose_name = _("Start Instances")
    url = "horizon:prof:courses:start_instances"
    classes = ("ajax-modal", "btn-launch")

    def allowed(self, request, instance=None):
        return True

# action to stop instances
class StopInstancesAction(tables.BatchAction):
    name = "stop instance"
    action_present = _("Stop")
    action_past = _("Stopped")
    data_type_singular = _("Instance")

    def allowed(self, request, instance=None):
       return True

    def action(self, request, obj_id):
        helper = CourseHelper()
        # TODO : we should not use getCourses() here. The course object should
        # be get by the action itself.
        courses = helper.getCourses()
        # stop all instances for a course.
        helper.stopInstances(courses[0])
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
	row_actions = (StartInstancesAction, StopInstancesAction,)
