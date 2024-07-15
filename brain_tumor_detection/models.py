from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Brain_Tumor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200, help_text="Give it a custom name", blank=True, null=True)
    photo = models.ImageField(upload_to='brain_tumor_images/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} Detection"