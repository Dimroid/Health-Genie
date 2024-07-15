from django.db import models
from django.conf import settings
from symptom_checker.models import SymptomChecker as Symptom

class HealthData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.FloatField(help_text="Body height in meters")
    age = models.IntegerField(help_text="Age in years")
    mass = models.FloatField(help_text="Body mass in kilograms")
    body_fat = models.FloatField(help_text="Body fat percentage", null=True, blank=True)

    workout_intensity_choices = [
        ('INTENSE', 'Intense'),
        ('NORMAL', 'Normal'),
        ('BODYBUILDING', 'Bodybuilding'),
        ('CALISTHENICS', 'Calisthenics'),
        ('OTHER', 'Other'),
    ]
    workout_intensity = models.CharField(max_length=50, choices=workout_intensity_choices, default='NORMAL')

    symptoms = models.ManyToManyField(Symptom, related_name='health_data')

    def __str__(self):
        return f"{self.user.username}'s Health Data"

class ExerciseRecommendation(models.Model):
    health_data = models.ForeignKey(HealthData, on_delete=models.CASCADE)
    recommendation = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Exercise Recommendation for {self.health_data.user.username} on {self.date}"
