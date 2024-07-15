from django.shortcuts import render, get_object_or_404
from django.core.files.storage import default_storage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from django.contrib.auth.decorators import login_required
import numpy as np
from .models import Brain_Tumor
from .forms import BrainTumorForm
import os

print("Current working directory:", os.getcwd())

# Load the trained model
model = load_model('brain_tumor_detection/brain_tumour_app/cancer_detection_model.h5')

@login_required
def index(request):
    form = BrainTumorForm()
    return render(request, 'brain_tumor.html', {'form': form, 'section':'Medical.D'})


@login_required
def predict(request):
    if request.method == 'POST':
        # Get the uploaded file from the form
        form = BrainTumorForm(request.POST, request.FILES)
        if form.is_valid():
            brain_tumor_instance = form.save()

            # Load the image for prediction from the Brain_Tumor model instance
            img_path = brain_tumor_instance.photo.path
            img = image.load_img(img_path, target_size=(64, 64))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to create batch size of 1

            # Preprocess the image
            img_array = img_array / 255.0

            # Make a prediction
            prediction = model.predict(img_array)
            if prediction[0][0] > 0.5:
                result = "The image contains brain tumor regions."
            else:
                result = "The image does not contain brain tumor regions."

            return render(request, 'brain_tumor.html', {'prediction': result, 'form': form, 'section':'Medical.D'})
    else:
        form = BrainTumorForm()

    return render(request, 'brain_tumor.html', {'form': form, 'section':'Medical.D'})
