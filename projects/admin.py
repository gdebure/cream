from projects.models import Project, Profile, Authorization, Deliverable, SubjectFamily, Subject, Task, DeliverableVolume
from django.contrib import admin

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Authorization)
admin.site.register(Deliverable)
admin.site.register(DeliverableVolume)
admin.site.register(SubjectFamily)
admin.site.register(Subject)
admin.site.register(Task)