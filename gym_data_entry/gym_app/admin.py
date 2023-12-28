# gym_data_entry/admin.py
from django.contrib import admin
from .models import MembershipData, DailyEntry

class MembershipDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'date_of_birth', 'address', 'date_of_joining', 'entry_time', 'payment', 'paid_by', 'created_by', 'plan_type', 'age')
    search_fields = ('name', 'contact_number')
    list_filter = ('date_of_birth', 'date_of_joining', 'entry_time', 'created_by', 'plan_type')
    ordering = ('name',)
    def age(self, obj):
        return obj.calculate_age()
    age.short_description = 'Age'

class DailyEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'entry_time')
    search_fields = ('name',)
    list_filter = ('entry_time',)
    date_hierarchy = 'entry_time'
    
admin.site.register(MembershipData, MembershipDataAdmin)
admin.site.register(DailyEntry, DailyEntryAdmin)