from django.db import models
from django.contrib.auth.models import User

class SymptomChecker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms = models.TextField()
    medical_history = models.TextField()
    age = models.IntegerField()
    duration = models.CharField(max_length=100, null=True, blank=True)
    severity = models.CharField(max_length=100, null=True, blank=True)
    Symptom_History = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    
    DURATION_CHOICES = (
        ('H', 'Hours'),
        ('D', 'Days'),
        ('W', 'Weeks'),
        ('M', 'Months'),
        ('Y', 'Years'),
    )
    
    SEVERITY_CHOICES = (
        ('M', 'Mild'),
        ('MO', 'Moderate'),
        ('S', 'Severe'),
    )
    
    duration = models.CharField(max_length=1, choices=DURATION_CHOICES)
    severity = models.CharField(max_length=2, choices=SEVERITY_CHOICES)
    Symptom_History = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Symptom Checker for {self.user.username}"
