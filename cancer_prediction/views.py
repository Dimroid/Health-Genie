from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CancerPredictionForm
import pickle
import numpy as np

# Load the model and scaler
with open('cancer_prediction/Breast_cancer_prediction_app/model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('cancer_prediction/Breast_cancer_prediction_app/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

def predict_cancer(input_features):
    input_features_scaled = scaler.transform(np.array([input_features]))
    prediction = model.predict(input_features_scaled)
    return prediction

@login_required
def cancer_prediction_view(request):
    if request.method == 'POST':
        form = CancerPredictionForm(request.POST)
        if form.is_valid():
            input_features = [
                form.cleaned_data['radius_mean'],
                form.cleaned_data['texture_mean'],
                form.cleaned_data['perimeter_mean'],
                form.cleaned_data['area_mean'],
                form.cleaned_data['smoothness_mean'],
                form.cleaned_data['compactness_mean'],
                form.cleaned_data['concavity_mean'],
                form.cleaned_data['concave_points_mean'],
                form.cleaned_data['symmetry_mean'],
                form.cleaned_data['fractal_dimension_mean'],
                form.cleaned_data['radius_se'],
                form.cleaned_data['texture_se'],
                form.cleaned_data['perimeter_se'],
                form.cleaned_data['area_se'],
                form.cleaned_data['smoothness_se'],
                form.cleaned_data['compactness_se'],
                form.cleaned_data['concavity_se'],
                form.cleaned_data['concave_points_se'],
                form.cleaned_data['symmetry_se'],
                form.cleaned_data['fractal_dimension_se'],
                form.cleaned_data['radius_worst'],
                form.cleaned_data['texture_worst'],
                form.cleaned_data['perimeter_worst'],
                form.cleaned_data['area_worst'],
                form.cleaned_data['smoothness_worst'],
                form.cleaned_data['compactness_worst'],
                form.cleaned_data['concavity_worst'],
                form.cleaned_data['concave_points_worst'],
                form.cleaned_data['symmetry_worst'],
                form.cleaned_data['fractal_dimension_worst'],
            ]
            prediction = predict_cancer(input_features)
            return render(request, 'result.html', {'prediction': prediction, 'section':'breast_cancers'})
    else:
        form = CancerPredictionForm()
    return render(request, 'form.html', {'form': form})
