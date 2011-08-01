from django import forms

from qualifications.models import Skill, SkillCategory, Job

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        

class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        
        
class JobForm(forms.ModelForm):
    class Meta:
        model = Job