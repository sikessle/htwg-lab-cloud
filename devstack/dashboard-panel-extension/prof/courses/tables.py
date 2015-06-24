from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables

from .course import Course
from .course import CourseHelper

# action to start instances
class StartInstancesAction(tables.LinkAction):
    name = "start instance"
    verbose_name = _("Instanzen starten")
    url = "horizon:prof:courses:start_instances"
    classes = ("ajax-modal", "btn-launch")

    def allowed(self, request, instance=None):
        return True

    def get_link_url(self, datum):
	# we add the id of the course as a query string to the url
        base_url = super(StartInstancesAction, self).get_link_url(datum)
        course_query_string = "course=" + datum.id
        print "?".join([base_url, course_query_string])
        return "?".join([base_url, course_query_string])

# action to stop instances
class StopInstancesAction(tables.BatchAction):
    name = "stop instance"

    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Instanzen stoppen",
            u"Instanzen stoppen",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Instanzen gestoppt",
            u"Instanzen gestoppt",
            count
        )

    def allowed(self, request, instance=None):
       return True

    def action(self, request, obj_id):
        # TODO : remove when we implemented moodle connection
        #import inspect
        #for x in inspect.getmembers(request.user):
        #    print x
        #print "USER_DATA_XX"
        #print request.user.id
        #print request.user.username
        #print request.user.token.id

        helper = CourseHelper(request.user)
        # stop all instances of the course.
        helper.stopInstances(courseId=obj_id)
        return True

# action to refresh course
class RefreshCourseAction(tables.BatchAction):
    name = "refresh course"

    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Kurs aktualisieren",
            u"Kurs aktualisieren",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Kurs aktualisiert",
            u"Kurs aktualisiert",
            count
        )

    def allowed(self, request, instance=None):
       return True

    def action(self, request, obj_id):
        helper = CourseHelper(request.user)
        # refresh all instances of the course.
        helper.refreshInstances(courseId=obj_id)
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
        verbose_name = _("Kurse")
	table_actions = (FilterAction,)
	row_actions = (StartInstancesAction, StopInstancesAction, RefreshCourseAction,)
