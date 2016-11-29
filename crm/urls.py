from django.conf.urls import patterns, url
from crm import views as v


urlpatterns = patterns(
    '',
    url(r'^(?P<model>(:?company|requirement))/list/$', v.List.as_view(), name='list'),
    url(r'^(?P<model>(:?company|requirement))/create/$', v.Create.as_view(), name='create'),
    url(r'^(?P<model>(:?company|requirement))/update/(?P<pk>\d+)/$', v.Update.as_view(), name='update'),
    url(r'^(?P<model>(:?company|requirement))/delete/(?P<pk>\d+)/$', v.Delete.as_view(), name='update'),
    url(r'^(?P<model>(:?company|requirement))/status/(?P<pk>\d+)/$', v.Status.as_view(), name='update'),
)
