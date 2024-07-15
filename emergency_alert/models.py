from django.db import models
from django.conf import settings

class EmergencyAlert(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    alert_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return f"Emergency alert for {self.user.username} at {self.timestamp}"
