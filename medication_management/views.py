from django.shortcuts import render, get_object_or_404, redirect
from .models import Medication, MedicationReminder
from .forms import MedicationForm, MedicationReminderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def medication_list(request):
    medications = Medication.objects.filter(user=request.user)  # Only show medications for the logged-in user
    return render(request, 'medication_management/medication_list.html', {'medications': medications})

@login_required
def medication_detail(request, pk):
    medication = get_object_or_404(Medication, pk=pk, user=request.user)  # Ensure the user is the owner of the medication
    return render(request, 'medication_management/medication_detail.html', {'medication': medication})

@login_required
def add_medication(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            medication = form.save(commit=False)
            medication.user = request.user  # Set the user field to the currently logged-in user
            medication.save()
            return redirect('medication_management:medication_list')  # Redirect to the medication list or any other appropriate view
    else:
        form = MedicationForm()
    return render(request, 'medication_management/add_medication.html', {'form': form})

@login_required
def add_reminder(request, medication_id):
    medication = get_object_or_404(Medication, id=medication_id, user=request.user)  
    if request.method == 'POST':
        form = MedicationReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.medication = medication
            reminder.save()
            messages.success(request, 'Reminder added successfully.')
            return redirect('medication_management:medication_detail', pk=medication_id)
        else:
            messages.error(request, 'Failed to add reminder. Please check the form.')
            print(form.errors)  
    else:
        form = MedicationReminderForm()
    return render(request, 'medication_management/add_reminder.html', {'form': form, 'medication': medication})

@login_required
def edit_medication(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    if request.method == 'POST':
        form = MedicationForm(request.POST, instance=medication)
        if form.is_valid():
            form.save()
            return redirect('medication_management:medication_detail', pk=pk)
    else:
        form = MedicationForm(instance=medication)
    return render(request, 'medication_management/edit_medication.html', {'form': form, 'medication': medication})

@login_required
def delete_reminder(request, reminder_id):
    reminder = get_object_or_404(MedicationReminder, id=reminder_id)
    medication_id = reminder.medication.id
    if request.method == 'POST':
        reminder.delete()
        messages.success(request, 'Reminder deleted successfully.')
        return redirect('medication_management:medication_detail', pk=medication_id)
    return render(request, 'medication_management/delete_reminder.html', {'reminder': reminder})


@login_required
def delete_medication(request, pk):
    medication = get_object_or_404(Medication, pk=pk, user=request.user)  # Ensure the user is the owner of the medication
    if request.method == 'POST':
        medication.delete()
        return redirect('medication_management:medication_list')
    return render(request, 'medication_management/delete_medication.html', {'medication': medication})
