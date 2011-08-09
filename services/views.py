from django.views.generic import UpdateView
from guardian.decorators import permission_required_or_403

from services.models import Domain

class DomainUpdateView(UpdateView):

    @permission_required_or_403('services.change_domain',(Domain, 'owner', 'user'))
    def dispatch(self, *args, **kwargs):
        return super(DomainUpdateView, self).dispatch(*args, **kwargs)
