from django.conf.urls import patterns, include, url
from django.contrib import admin
from crm import urls as crm



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dsmanagement.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^masterdata/', include(crm)),
    url(r'^admin/', include(admin.site.urls)),  
    url(r'^logout/$','users.user_logout',name="home"),
	url(r'^$','users.user_login',name="home"),
    url(r'^home/$','crm.views.home',name="home"),
    url(r'^org-list/$','crm.views.org_list',name="home"),
    url(r'^sales-list/$','crm.views.sales',name="home"),
    url(r'^company-list/$','crm.views.company_list',name="home"),
    url(r'^company_info/(?P<pid>\d+)$','crm.views.company_info',name="home"),
    url(r'^recur_info/$','crm.views.recur_info',name='home')

    
    
)
