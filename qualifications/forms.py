from django import forms

from qualifications.models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        