from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^directory/admin/', include(admin.site.urls)),	
    url(r'^directory/', include('web.urls', namespace='directory')),
)
