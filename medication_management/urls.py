from django.urls import path
from . import views

app_name = 'medication_management'

urlpatterns = [
    path('', views.medication_list, name='medication_list'),
    path('medication/<int:pk>/', views.medication_detail, name='medication_detail'),
    path('medication/add/', views.add_medication, name='add_medication'),
    path('medication/<int:medication_id>/add_reminder/', views.add_reminder, name='add_reminder'),
    path('medication/<int:pk>/edit/', views.edit_medication, name='edit_medication'),
    path('medication/<int:pk>/delete/', views.delete_medication, name='delete_medication'),
    path('reminder/<int:reminder_id>/delete/', views.delete_reminder, name='delete_reminder'),

]
