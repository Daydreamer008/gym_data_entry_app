# gym_app/urls.py
from django.urls import path
from .views import membership_form, daily_entry_form,membership_form_success 

urlpatterns = [
    path('membership-form/', membership_form, name='membership_form'),
    path('daily-entry-form/', daily_entry_form, name='daily_entry_form'),
    path('membership-form-success/', membership_form_success, name='membership_form_success'),
]
