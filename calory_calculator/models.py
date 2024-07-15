from django.db import models
from django.conf import settings

class FoodImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='food_images/', blank=True, null=True)
    food_name = models.CharField(max_length=100, blank=True, null=True)
    grams = models.FloatField(blank=True, null=True)
    calories = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.food_name} ({self.grams}g)"

    def get_human_readable_food_name(self):
        food_name_mapping = {
            'class1': 'amala',
            'class2': 'eba',
            'class3': 'garri',
            'class4': 'indomie',
            'class5': 'rice',
            'class6': 'spaghetti',
        }
        return food_name_mapping.get(self.food_name, self.food_name)
