# gym_app/forms.py
from django import forms
from .models import MembershipData, DailyEntry

class MembershipDataForm(forms.ModelForm):
    class Meta:
        model = MembershipData
        fields = '__all__'

class DailyEntryForm(forms.ModelForm):
    class Meta:
        model = DailyEntry
        fields = '__all__'
