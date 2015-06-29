from django.contrib import admin

from recruitment.models import Applicant, ApplicantPosition, InterviewType, InterviewStatus, Interview

admin.site.register(Applicant)
admin.site.register(ApplicantPosition)
admin.site.register(InterviewType)
admin.site.register(InterviewStatus)
admin.site.register(Interview)