from django.conf.urls import include, url

from django.contrib.auth.decorators import login_required

from .views import HomeView, DashboardView

# Enable the admin site:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Base URL displays home page
    # url(r'^$', login_required()(HomeView.as_view()),name="home"),
    url(r'^$', DashboardView.as_view()),
    
    # URL for the admin site:
    url(r'^admin/', include(admin.site.urls)),
    
    # URL for the comments framework
    url(r'^comments/', include('django_comments.urls')),
    
    # URLs for applications
    url(r'^services/',include('services.urls')),
    url(r'^projects/',include('projects.urls')),
    url(r'^reports/',include('reports.urls')),
    url(r'^users/',include('users.urls')),
    url(r'^qualifications/',include('qualifications.urls')),
    url(r'^recruitment/',include('recruitment.urls')),
]
