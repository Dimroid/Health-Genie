from django.contrib import admin
from .models import Profile, Additional_Info

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'bio', 'photo', 'country', 'state', 'phone_number', 'city', 'zipcode']

@admin.register(Additional_Info)
class Additional_Info_Admin(admin.ModelAdmin):
    list_display = ['age', 'gender', 'medical_history', 'additional_information']
