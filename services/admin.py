from services.models import Domain, ServiceFamily, Service
from django.contrib import admin
from guardian.admin import GuardedModelAdmin

class DomainAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

class ServiceFamilyAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...
    
class ServiceAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

admin.site.register(Domain, DomainAdmin)
admin.site.register(ServiceFamily, ServiceFamilyAdmin)
admin.site.register(Service, ServiceAdmin)