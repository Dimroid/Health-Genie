from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

app_name = 'symptom_checker'

urlpatterns = [
    path('', views.symptom_checker, name='symptom'),
]