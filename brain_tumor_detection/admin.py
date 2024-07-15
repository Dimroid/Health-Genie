from django.contrib import admin
from .models import Brain_Tumor

@admin.register(Brain_Tumor)
class BrainTumorAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')

