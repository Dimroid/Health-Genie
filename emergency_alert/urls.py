from django.urls import path
from . import views

app_name = 'disease_outbreak'

urlpatterns = [
    path('', views.index, name='index'),
]
