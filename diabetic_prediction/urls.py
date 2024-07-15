from django.urls import path
from . import views

app_name = 'diabetic_prediction'

urlpatterns = [
    path('', views.index, name='default'),
    path('predict/', views.predict, name='diabetic_predict'),
]
