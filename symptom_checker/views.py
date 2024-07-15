from meta_ai_api import MetaAI
from django.conf import settings
from django.shortcuts import render
from .forms import SymptomCheckerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import Additional_Info, Profile

def get_meta_ai_response(prompt):
    ai = MetaAI()
    response = ai.prompt(message=prompt)
    return response['message']

@login_required
def symptom_checker(request):
    if request.method == 'POST':
        form = SymptomCheckerForm(request.POST)
        if form.is_valid():
            symptom_checker_instance = form.save(commit=False)
            symptom_checker_instance.user = request.user

            try:
                # Fetch additional info if it exists
                additional_info = Additional_Info.objects.get(user=request.user)
                symptom_checker_instance.age = additional_info.age
            except Additional_Info.DoesNotExist:
                # Set age to None and notify the user
                symptom_checker_instance.age = None
                messages.error(request, 'Age information not found. Please update your profile.')
                
            # Populate the missing fields
            symptom_checker_instance.age = additional_info.age
            symptom_checker_instance.state = Profile.state
            # Add other fields as necessary

            symptom_checker_instance.save()

            # Prepare the prompt for Meta AI
            prompt = (f"Symptoms: {symptom_checker_instance.symptoms}, Medical History: "
                      f"{symptom_checker_instance.medical_history}, Age: {symptom_checker_instance.age if symptom_checker_instance.age else 22}, "
                      f"Duration: {symptom_checker_instance.duration}, Severity: {symptom_checker_instance.severity}, "
                      f"Symptom History: {symptom_checker_instance.Symptom_History}, "
                    #   f"Please provide a possible diagnosis."
                      )
            
            # Get the response from Meta AI
            meta_ai_response = get_meta_ai_response(prompt)
            
            import logging

            # Set up logging
            logger = logging.getLogger(__name__)

            # In your view function
            logger.info(f"AI Response: {meta_ai_response}")
            
            return render(request, 'meta_ai_symptom_response.html', {'ai_response': meta_ai_response, 'section': 'symptom'})
        else:
            messages.error(request, 'Error updating your profile')
    else:
        form = SymptomCheckerForm()

    context = {
        'form': form,
        'section': 'symptom'  # Ensures the sidebar highlights correctly
    }
    return render(request, 'symptom_checker.html', context)
