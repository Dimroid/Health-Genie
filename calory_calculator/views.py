# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FoodImageForm
from .models import FoodImage
import cv2
import os
from tensorflow.keras.models import load_model
import numpy as np
from meta_ai_api import MetaAI

# Load the trained food recognition model
model = load_model('Food_Images_Train/food_recognition_model.h5')

def food_recognition(image_path, confidence_threshold=0.2):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Failed to load image from path: {image_path}")
    resized_img = cv2.resize(img, (150, 150))
    rgb_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
    rgb_img = rgb_img.astype('float') / 255.0
    rgb_img = np.expand_dims(rgb_img, axis=0)

    # Use the model to make predictions
    predictions = model.predict(rgb_img)
    predicted_class = np.argmax(predictions[0])
    confidence = predictions[0][predicted_class]

    # Map the predicted class to a food label
    class_labels = {
        0: 'amala',
        1: 'eba',
        2: 'garri',
        3: 'indomie',
        4: 'rice',
        5: 'spaghetti',
    }
    
    if confidence >= confidence_threshold:
        predicted_label = class_labels.get(predicted_class, 'Unknown')
    else:
        predicted_label = 'Unknown'
    
    return predicted_label

def get_meta_ai_response(food_name, grams):
    ai = MetaAI()
    prompt = f"Give me the calorie information for {grams} grams of {food_name}"
    response = ai.prompt(message=prompt)
    return response['message']

@login_required
def upload_food_image(request):
    if request.method == 'POST':
        form = FoodImageForm(request.POST, request.FILES)
        if form.is_valid():
            grams = form.cleaned_data['grams']
            food_image = form.save(commit=False)
            food_image.user = request.user 
            food_image.save()  # Save the image first
            image_path = food_image.photo.path  # Get the correct path to the saved image
            
            try:
                predicted_label = food_recognition(image_path)
                if predicted_label != 'Unknown':
                    calorie_info = get_meta_ai_response(predicted_label, grams)
                    calories = extract_calories(calorie_info)
                    food_image.food_name = predicted_label
                    food_image.calories = calories
                    print(calorie_info)
                    additional_info = calorie_info
                    food_image.additional_info = additional_info
                    food_image.save()  # Save the predicted food name
                    messages.success(request, 'Image uploaded and food recognized successfully.')
                    return redirect('calory_calculator:food_image_detail', pk=food_image.pk)
                elif predicted_label == 'Unknown':
                    food_image.food_name = 'Unknown'
                    food_image.calories = 'Null'
                    additional_info = "Null"
                    food_image.additional_info = "Null"
                    food_image.save()  # Save the predicted food name
                    messages.error(request, 'Could not recognize the food in the uploaded image..')
                    return redirect('calory_calculator:food_image_detail', pk=food_image.pk)
                else:
                    messages.error(request, 'Could not recognize the food in the uploaded image.')
            except ValueError as e:
                messages.error(request, f'Error in processing image: {e}')
                
            return redirect('calory_calculator:food_image_detail', pk=food_image.pk)
    else:
        form = FoodImageForm()
    return render(request, 'calory_checker.html', {'form': form, 'section': 'calories'})

@login_required
def food_image_detail(request, pk):
    food_image = get_object_or_404(FoodImage, pk=pk)
    calorie_info = request.GET.get('calorie_info', None)
    return render(request, 'calory_checker_detail.html', {'food_image': food_image, 'calorie_info': calorie_info, 'section': 'calories'})

def extract_calories(calorie_info):
    try:
        # Assuming the calorie_info string contains the calorie information in the format: "contains approximately XXX calories."
        start_index = calorie_info.find('approximately') + len('approximately')
        end_index = calorie_info.find('calories')
        calorie_amount = calorie_info[start_index:end_index].strip()
        return float(calorie_amount)
    except:
        return 'result is in the additional information'