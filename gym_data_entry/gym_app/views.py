# gym_app/views.py
from django.shortcuts import render, redirect
from .forms import MembershipDataForm, DailyEntryForm
from datetime import datetime  

def membership_form(request):
    if request.method == 'POST':
        form = MembershipDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership_form_success')  
    else:
        form = MembershipDataForm()
    
    return render(request, 'membership_form.html', {'form': form})

def daily_entry_form(request):
    if request.method == 'POST':
        form = DailyEntryForm(request.POST)
        if form.is_valid():
            form.instance.entry_time = datetime.now()
            form.save()
            return redirect('membership_form_success')  
    else:
        form = DailyEntryForm()
    
    return render(request, 'daily_entry_form.html', {'form': form})

def membership_form_success(request):
    return render(request, 'membership_form_success.html')  