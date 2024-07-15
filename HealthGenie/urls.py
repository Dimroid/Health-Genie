from django.contrib import admin
from django.urls import path, include
from account import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from account.views import error_404_view

handler404 = error_404_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', views.home, name='home'),
    path('symptoms/', include('symptom_checker.urls')),
    path('calory_calculator/', include('calory_calculator.urls')),
    path('brain_tumour/', include('brain_tumor_detection.urls')),
    path('cancer_prediction/', include('cancer_prediction.urls')),
    path('messaging/', include('messaging.urls')),
    path('diabetes_prediction/', include('diabetic_prediction.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('disease_outbreak/', include('emergency_alert.urls')),
    path('medication_management/', include('medication_management.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
