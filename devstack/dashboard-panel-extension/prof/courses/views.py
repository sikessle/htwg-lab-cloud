from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions, tables, workflows, forms, tabs
import json
from .tables import CoursesTable
from .course import Course
from .course import CourseHelper

from horizon.utils import memoized

from openstack_dashboard.dashboards.prof.courses \
    import forms as project_forms
    
from openstack_dashboard.dashboards.prof.courses.workflows.create_instance import LaunchInstance

class CoursesTableView(tables.DataTableView):
    # A very simple class-based view...
    table_class = CoursesTable
    template_name = 'prof/courses/index.html'

    def get_data(self):
        helper = CourseHelper(self.request.user)
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

class LaunchInstanceView(workflows.WorkflowView):
    workflow_class = LaunchInstance

    def get_initial(self):
        initial = super(LaunchInstanceView, self).get_initial()
        # FIXME : We pass course as a query parameter to get it available in create_instance.py
        # This method get's called on creation of the input form and after clicking the submit button.
        # On the first call 'course' is available, but on the second it's None. However we expected that
        # get_initial will only be called once and not twice.        
        # course should be the same as tenant_id, but tenant_id is set to the actual active tenant.
        initial['project_id'] = initial.get('course', self.request.user.tenant_id)
        initial['user_id'] = self.request.user.id
        return initial


