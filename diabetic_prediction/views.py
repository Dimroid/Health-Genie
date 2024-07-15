from django.shortcuts import render
from django.core.files.storage import default_storage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from django.contrib.auth.decorators import login_required
import numpy as np
from .models import Diabetic_Prediction
from .forms import DiabeticPredictionForm

# Load the trained model
model = load_model('diabetic_prediction/diabetic_app/diabetic_retinopathy_model.h5')
# Determine the expected input shape of the model
input_shape = model.input_shape[1:3]  # (height, width)

@login_required
def index(request):
    form = DiabeticPredictionForm()
    return render(request, 'diabetes_checker.html', {'form': form, 'section': 'Medical.D'})

@login_required
def predict(request):
    if request.method == 'POST':
        form = DiabeticPredictionForm(request.POST, request.FILES)
        if form.is_valid():
            diabetic_prediction_instance = form.save(commit=False)
            if 'photo' in request.FILES:
                diabetic_prediction_instance.photo = request.FILES['photo']
                diabetic_prediction_instance.save()

                # Load the image for prediction from the Diabetic_Prediction model instance
                img_path = diabetic_prediction_instance.photo.path
                img = image.load_img(img_path, target_size=input_shape)  # Adjusting target_size dynamically
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to create batch size of 1

                # Preprocess the image
                img_array = img_array / 255.0

                # Make a prediction
                prediction = model.predict(img_array)
                if prediction[0][0] > 0.5:
                    result = "The image shows you have a high likelihood of diabetes."
                else:
                    result = "The image shows you have a low likelihood of diabetes."

                return render(request, 'diabetes_checker.html', {'prediction': result, 'form': form, 'section': 'Medical.D'})
            else:
                form.add_error('photo', 'No file uploaded.')
        else:
            form.add_error(None, 'Form is not valid.')
    else:
        form = DiabeticPredictionForm()

    return render(request, 'diabetes_checker.html', {'form': form, 'section': 'Medical.D'})
