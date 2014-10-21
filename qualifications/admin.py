from qualifications.models import SkillCategory, Skill, Job, Location, Position, Profile, EmployeeSkill, JobProfileSkill, EmployeePositionStatus ,EmployeePosition
from django.contrib import admin
from guardian.admin import GuardedModelAdmin

class SkillCategoryAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

class SkillAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

class JobAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

class LocationAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

class PositionAdmin(GuardedModelAdmin):
    pass #Nothing to do here yet...

class ProfileAdmin(GuardedModelAdmin):
    pass

class EmployeeSkillAdmin(GuardedModelAdmin):
    pass

class JobProfileSkillAdmin(GuardedModelAdmin):
    pass

class EmployeePositionStatusAdmin(GuardedModelAdmin):
    pass

class EmployeePositionAdmin(GuardedModelAdmin):
    pass

admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Position,PositionAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(EmployeeSkill, EmployeeSkillAdmin)
admin.site.register(JobProfileSkill, JobProfileSkillAdmin)
admin.site.register(EmployeePositionStatus, EmployeePositionStatusAdmin)
admin.site.register(EmployeePosition, EmployeePositionAdmin)