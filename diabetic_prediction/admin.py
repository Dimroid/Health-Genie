from django.contrib import admin
from .models import Diabetic_Prediction

@admin.register(Diabetic_Prediction)
class DiabeticPredictionAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')

