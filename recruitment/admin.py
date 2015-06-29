from django.contrib import admin

from recruitment.models import Applicant, ApplicantPosition, RecruitmentMeetingType, RecruitmentMeetingStatus, RecruitmentMeeting

admin.site.register(Applicant)
admin.site.register(ApplicantPosition)
admin.site.register(RecruitmentMeetingType)
admin.site.register(RecruitmentMeetingStatus)
admin.site.register(RecruitmentMeeting)