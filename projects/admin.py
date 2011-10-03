from projects.models import Project, Profile, Authorization, Deliverable, SubjectFamily, Subject, Task, DeliverableVolume
from django.contrib import admin
from guardian.admin import GuardedModelAdmin

class ProjectAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile)
admin.site.register(Authorization)
admin.site.register(Deliverable)
admin.site.register(DeliverableVolume)
admin.site.register(SubjectFamily)
admin.site.register(Subject)
admin.site.register(Task)