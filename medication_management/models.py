from django.db import models
from django.contrib.auth.models import User

class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

class MedicationReminder(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='reminders')
    reminder_time = models.TimeField()
    notes = models.TextField()  # Add a field for notes
