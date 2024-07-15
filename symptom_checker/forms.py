# forms.py

from django import forms
from .models import SymptomChecker

class SymptomCheckerForm(forms.ModelForm):
    class Meta:
        model = SymptomChecker
        fields = ['duration', 'severity', 'symptoms', 'Symptom_History']
