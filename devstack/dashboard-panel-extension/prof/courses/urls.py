from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.prof.courses import views


urlpatterns = patterns('',
    url(r'^$',
        views.CoursesTableView.as_view(), name='index'),
    url(r'^(?P<course_id>[^/]+)/start_instances/$',
        views.StartInstancesView.as_view(),
        name='start_instances'),
)
