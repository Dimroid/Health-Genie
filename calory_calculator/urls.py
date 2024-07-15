from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'calory_calculator'

urlpatterns = [
    path('food_upload/', views.upload_food_image, name='calory'),
    path('image/<int:pk>/', views.food_image_detail, name='food_image_detail'),
]

