from django.urls import path
from . import views

app_name = 'brain_tumor_detection'

urlpatterns = [
    path('', views.index, name='default'),
    path('predict/', views.predict, name='predict'),
]
