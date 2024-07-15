from django.contrib import admin
from .models import Medication, MedicationReminder

class MedicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'dosage', 'frequency', 'start_date', 'end_date')
    search_fields = ('name', 'user__username')
    list_filter = ('user', 'start_date', 'end_date')

class MedicationReminderAdmin(admin.ModelAdmin):
    list_display = ('medication', 'reminder_time')
    search_fields = ('medication__name', 'medication__user__username')
    list_filter = ('reminder_time',)

admin.site.register(Medication, MedicationAdmin)
admin.site.register(MedicationReminder, MedicationReminderAdmin)
