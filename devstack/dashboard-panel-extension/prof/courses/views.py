from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import tables
import json
from .tables import CoursesTable
from .course import Course
from .course import CourseHelper

from horizon import exceptions
from horizon import forms

from horizon.utils import memoized

from openstack_dashboard.dashboards.prof.courses \
    import forms as project_forms

class CoursesTableView(tables.DataTableView):
    # A very simple class-based view...
    table_class = CoursesTable
    template_name = 'prof/courses/index.html'


    def get_data(self):
	helper = CourseHelper()
	return helper.getCourses()

class StartInstancesView(forms.ModalFormView):
    form_class = project_forms.StartInstances
    template_name = 'prof/courses/start_instances.html'
    success_url = reverse_lazy("horizon:prof:courses:index")
    modal_id = "start_instances_modal"
    modal_header = _("Start Instances")
    submit_label = _("Create VMs")
    submit_url = "horizon:prof:courses:start_instances"

    @memoized.memoized_method
    def get_object(self):
       course_id = self.kwargs['course_id']
       try:
         print course_id
       except Exception:
         redirect = self.success_url
         msg = _('Unable to retrieve course.')
         exceptions.handle(self.request, msg, redirect=redirect)



    def get_initial(self):
        return {"course_id": self.kwargs["course_id"]}

    def get_context_data(self, **kwargs):
        context = super(StartInstancesView, self).get_context_data(**kwargs)
        context['course_id'] = self.kwargs['course_id']
       # context['course_id'] = instance_id
       # context['course'] = self.get_object()
        #context['submit_url'] = reverse(self.submit_url, args=[instance_id])
        return context



