from django import forms

from qualifications.models import Skill, SkillCategory, Job, Profile

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        

class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        
        
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile