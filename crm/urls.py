from django.conf.urls import patterns, url
from crm import views as v



urlpatterns = patterns(
    '',
    url(r'^(?P<model>(:?company))/list/$', v.List.as_view(), name='list'),
    url(r'^(?P<model>(:?requirement))/list/(?P<pk>.*)$', v.List.as_view(), name='list'),
    url(r'^(?P<model>(:?company))/create/$', v.Create.as_view(), name='create'),
    url(r'^(?P<model>(:?requirement))/create/(?P<pk>.*)/$', v.Create.as_view(), name='create'),
    url(r'^(?P<model>(:?company|requirement))/update/(?P<pk>\d+)/$', v.Update.as_view(), name='update'),
    url(r'^(?P<model>(:?company|requirement))/delete/(?P<pk>\d+)/$', v.Delete.as_view(), name='update'),
    url(r'^(?P<model>(:?company|requirement))/status/(?P<pk>\d+)/$', v.Status.as_view(), name='update'),

    url(r'^(?P<model>(:?profile|employeeinfo))/list/$', v.List.as_view(), name='list'),
    url(r'^(?P<model>(:?profile|employeeinfo))/create/$', v.Create.as_view(), name='create'),
    url(r'^(?P<model>(:?profile|employeeinfo))/status/$', v.Status.as_view(), name='create'),
)
