from django.urls import path
from cancer_prediction.views import cancer_prediction_view

app_name='cancer_prediction'

urlpatterns = [
    path('predict/', cancer_prediction_view, name='breast_cancer'),
]
