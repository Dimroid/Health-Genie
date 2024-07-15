from django import forms
from django.contrib.auth.models import User
from .models import Diabetic_Prediction

class DiabeticPredictionForm(forms.ModelForm):
    class Meta:
        model = Diabetic_Prediction
        fields = {'name', 'photo'}
        