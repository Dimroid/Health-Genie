from django import forms
from django.core.exceptions import ValidationError
from .models import Medication, MedicationReminder

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'frequency', 'start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and end_date < start_date:
            raise ValidationError("End date cannot be older than the start date.")

class MedicationReminderForm(forms.ModelForm):
    class Meta:
        model = MedicationReminder
        fields = ['reminder_time', 'notes']
