from django.conf.urls import url, patterns

from reports.views import DomainsReportView, DomainReportView, ServiceFamilyReportView, ServiceReportView
from django.views.generic import TemplateView


urlpatterns = patterns('',
    ##################################
    # Reports
    url(r'^$',DomainsReportView.as_view(), name='domains_report'),
    url(r'^domains/(?P<pk>\d+)/$',DomainReportView.as_view(), name='domain_report'),
    url(r'^servicefamily/(?P<pk>\d+)/$', ServiceFamilyReportView.as_view(), name='servicefamily_report'),
    url(r'^service/(?P<pk>\d+)/$', ServiceReportView.as_view(), name='service_report'),
    ##################################
    )
    