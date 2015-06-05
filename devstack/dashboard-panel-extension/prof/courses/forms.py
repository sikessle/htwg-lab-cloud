from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms

from openstack_dashboard import api

from .course import Course
from .course import CourseHelper

class StartInstances(forms.SelfHandlingForm):
    name = forms.CharField(max_length="255", label=_("Name"))
    other = forms.CharField(widget=forms.Textarea,
            label=_("Other"), required=False)

    def __init__(self, request, *args, **kwargs):
        super(StartInstances, self).__init__(request, *args, **kwargs)


    def handle(self, request, data):
        try:
            helper = CourseHelper()
            # TODO : we should not use getCourses() here. The course object should
            # be get by the action itself.
            courses = helper.getCourses()
            # start all instances for a course.
            helper.startInstances(courses[0], imageName="cirros-0.3.4-x86_64-uec", flavorName="m1.tiny")

            message = _('Creating Form')
            messages.info(request, message)
            return True
        except Exception:
            redirect = reverse("horizon:prof:courses:index")
            exceptions.handle(request,
                              _('Unable to create Workload.'),
                              redirect=redirect)
