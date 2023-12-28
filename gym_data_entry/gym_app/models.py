# gym_data_entry/models.py
from django.db import models
from datetime import date

class MembershipData(models.Model):
    # Choices for trainer name
    TRAINER_NAME_CHOICES = [
        ('Amit', 'Amit'),
        ('Aditya', 'Aditya'),
    ]
    # Choices for plan type
    PLAN_TYPE_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Half-year', 'Half-year'),
        ('Yearly', 'Yearly'),
    ]
    # Choices for mode of payment
    MODE_OF_PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('Upi', 'Upi'),
    ]
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=False, blank=False)
    date_of_joining = models.DateField(null=False, blank=False)
    address = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    entry_time = models.DateTimeField(auto_now_add=True)
    payment = models.CharField(max_length=10, null=False, blank=False, help_text="Specify the payment amount.")
    paid_by = models.CharField(max_length=5, choices=MODE_OF_PAYMENT_CHOICES, default='------', null=False, blank=False, help_text="Choose the mode of payment.")
    created_by = models.CharField(max_length=10, choices=TRAINER_NAME_CHOICES, default='------', null=False, blank=False, help_text="Select the trainer.")
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPE_CHOICES, default='------', null=False, blank=False, help_text="Select the plan type.")

    # Methods for MembershipData model
    def calculate_age(self):
        today = date.today()
        if self.date_of_birth:
            age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            return age
        return None  # Handle case where date_of_birth is None

    def __str__(self):
        formatted_date_of_birth = self.date_of_birth.strftime('%d-%m-%Y') if self.date_of_birth else ''
        return f"{self.name} - DOB: {formatted_date_of_birth}, Age: {self.calculate_age()}, Plan Type: {self.plan_type}"

class DailyEntry(models.Model):
    #Entry type
    ENTRY_TYPE = [
        ('Regular', 'Regular'),
        ('Guest', 'Guest')
    ]

    name = models.CharField(max_length=100)
    entry_time = models.DateTimeField(auto_now_add=True)
    visit_type = models.CharField(max_length=10, choices=ENTRY_TYPE, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.entry_time} - {self.visit_type}"
