from django.conf.urls import url

from django.contrib.auth.views import login, logout_then_login, password_change, password_change_done

from users.views import EmployeeListView, FilteredEmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView
from qualifications.views import AddEmployeePositionFromEmployeeView

from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    ###################################
    # Authentication stuff
    url(r'^login/', login, {'template_name': 'login.html'}, name='login' ),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^change_password/$', password_change, {'template_name': 'password_change_form.html','post_change_redirect' : 'change_password/done/'}, name='change_password' ),
    url(r'^change_password/done/$', password_change_done, {'template_name': 'password_change_done.html'}, name='password_changed' ),
    ###################################
    
    url(r'^employees/$', EmployeeListView.as_view(), name='employees_list'),
    url(r'^employees/(?P<pk>\d+)/$', EmployeeDetailView.as_view(),name='employee'),
    url(r'^employees/create/$', EmployeeCreateView.as_view(), name='create_employee' ),
    url(r'^employees/(?P<pk>\d+)/update/$', EmployeeUpdateView.as_view(), name='update_employee' ),
    url(r'^employees/(?P<pk>\d+)/delete/$', EmployeeDeleteView.as_view(), name='delete_employee' ),
    
    url(r'^employees/(?P<pk>\d+)/add_position/$', AddEmployeePositionFromEmployeeView.as_view(), name='add_position_to_employee'),
    url(r'^employees/(?P<filter>.+)/$', FilteredEmployeeListView.as_view(),name='employees_list_status'),
]