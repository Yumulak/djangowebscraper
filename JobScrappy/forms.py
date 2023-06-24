from django import forms
from JobScrappy.models import Users

class ScheduleScrapesForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = ("name", "email", "urllist", "interval",)