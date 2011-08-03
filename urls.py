from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CREAM.views.home', name='home'),
    # url(r'^CREAM/', include('CREAM.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^services/',include('services.urls')),
    url(r'^tasks/',include('tasks.urls')),
    url(r'^employees/',include('users.urls')),
    url(r'^subjects/',include('subjects.urls')),
    url(r'^qualifications/',include('qualifications.urls')),
)
