from tasks.models import RequestorType, Task, Comment
from django.contrib import admin


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','name','open_date','deliverable','status')
    search_fields = ('id','name')

admin.site.register(RequestorType)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment)

