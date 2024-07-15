from django.contrib import admin
from .models import FoodImage

@admin.register(FoodImage)
class FoodImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_name', 'grams', 'calories', 'uploaded_at')
    search_fields = ('food_name',)
    list_filter = ('uploaded_at',)
