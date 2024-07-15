from django import forms
from django.contrib.auth.models import User
from .models import Brain_Tumor

class BrainTumorForm(forms.ModelForm):
    class Meta:
        model = Brain_Tumor
        fields = {'name', 'photo'}
        