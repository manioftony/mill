from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dsmanagement.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^logout/$','users.user_logout',name="home"),
    
    url(r'^$','users.user_login',name="home"),
    
    
    url(r'^home/$','crm.views.home',name="home"),
    url(r'^org-list/$','crm.views.org_list',name="home"),
    
    
)
