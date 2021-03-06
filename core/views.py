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
        return permission_required(view,cls.permission)
    
    
class PieChartMixin(object):
 
    data = dict()
    chartcontainer = 'piechart_container'

    @classmethod
    def set_chart(self,x_data,y_data):
        chartdata = {'x': x_data, 'y': y_data}
        charttype = "pieChart"
        self.data = {
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': self.chartcontainer,
            'extra': {
                'pieLabelsOutside':True,
            }
        }
        return self.data
