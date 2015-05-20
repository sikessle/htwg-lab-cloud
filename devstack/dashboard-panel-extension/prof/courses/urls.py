from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.prof.courses import views


urlpatterns = patterns('',
    url(r'^$',
        views.CoursesTableView.as_view(), name='index'),
#    url(r'^(?P<instance_id>[^/]+)/create_snapshot/$',
#        views.CreateSnapshotView.as_view(),
#        name='create_snapshot'),
)
