from projects.models import Project, Profile, Authorization, Deliverable, SubjectFamily, Subject, Task, DeliverableVolume
from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from reversion import VersionAdmin

class ProjectAdmin(GuardedModelAdmin, VersionAdmin):
    pass #Nothing to do here yet...

class DeliverableAdmin(GuardedModelAdmin, VersionAdmin):
    pass #Nothing to do here yet...

class DeliverableVolumeAdmin(GuardedModelAdmin, VersionAdmin):
    pass #Nothing to do here yet...

admin.site.register(Project, ProjectAdmin)
admin.site.register(Deliverable, DeliverableAdmin)
admin.site.register(DeliverableVolume, DeliverableVolumeAdmin)
admin.site.register(SubjectFamily)
admin.site.register(Subject)
admin.site.register(Task)