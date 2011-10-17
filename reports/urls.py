from django.conf.urls.defaults import *

from reports.models import Report
from django.views.generic import DetailView, ListView, CreateView, DeleteView


urlpatterns = patterns('',
    ##################################
    # Reports
    (r'^reports/create$', login_required()(CreateView.as_view( model=Report )), ),
    ##################################
    )
    