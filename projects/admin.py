from projects.models import ProjectStatus, Project, Deliverable, DeliverableVolume
from django.contrib import admin

admin.site.register(ProjectStatus)
admin.site.register(Project)
admin.site.register(Deliverable)
admin.site.register(DeliverableVolume)