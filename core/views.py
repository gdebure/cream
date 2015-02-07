from django.contrib.auth.decorators import login_required, permission_required

class LoginRequiredMixin(object):
    
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
    
class PermissionRequiredMixin(object):
    permission = None
    
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(PermissionRequiredMixin, cls).as_view(**initkwargs)
        return permission_required(view,self.permission)

    
class PieChartMixin(object):

    @classmethod
    def set_chart(self,x_data,y_data):
        chartdata = {'x': x_data, 'y': y_data}
        charttype = "pieChart"
        chartcontainer = 'piechart_container'
        data = {
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                'pieLabelsOutside':True,
            }
        }
        return data