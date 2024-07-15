from django import forms
from .models import FoodImage

class FoodImageForm(forms.ModelForm):
    class Meta:
        model = FoodImage
        fields = ['photo', 'grams']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'grams': forms.NumberInput(attrs={'class': 'form-control'}),
        }
