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