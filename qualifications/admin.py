from qualifications.models import SkillCategory, Skill, Job, Location, PositionStatus, Position, Profile, EmployeeSkill, JobProfileSkill, EmployeePositionStatus ,EmployeePosition
from django.contrib import admin

admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(PositionStatus)
admin.site.register(Position)
admin.site.register(Profile)
admin.site.register(EmployeeSkill)
admin.site.register(JobProfileSkill)
admin.site.register(EmployeePositionStatus)
admin.site.register(EmployeePosition)