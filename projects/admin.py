from projects.models import Project, Deliverable, SubjectFamily, Subject, Task, DeliverableVolume
from django.contrib import admin
from guardian.admin import GuardedModelAdmin

class ProjectAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

class DeliverableAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

class DeliverableVolumeAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

admin.site.register(Project)#, ProjectAdmin)
admin.site.register(Deliverable, DeliverableAdmin)
admin.site.register(DeliverableVolume, DeliverableVolumeAdmin)
admin.site.register(SubjectFamily)
admin.site.register(Subject)
admin.site.register(Task)