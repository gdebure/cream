from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib.auth.decorators import login_required

# Enable the admin site:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Base URL displays home page
    url(r'^$', login_required()(direct_to_template), {'template': 'home.html'}),

    # URL for the admin site:
    url(r'^admin/', include(admin.site.urls)),
    
    # URLs for applications
    url(r'^services/',include('services.urls')),
    url(r'^projects/',include('projects.urls')),
    url(r'^users/',include('users.urls')),
    url(r'^qualifications/',include('qualifications.urls')),
)
