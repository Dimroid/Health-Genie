from django.contrib import admin
from .models import SymptomChecker

@admin.register(SymptomChecker)
class SymptomCheckerAdmin(admin.ModelAdmin):
    list_display = ['symptoms', 'duration', 'severity', 'Symptom_History']

