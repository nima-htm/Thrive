from django.contrib import admin
from .models import Appointments  

class CustomApoAdmin(admin.ModelAdmin):  
    list_display = ("advisor_name", "appointment_time","status","patient")
    list_filter = ("status",)
    fields = ("advisor", "appointment_time",)
    
    def advisor_name(self, obj):
        return f"{obj.advisor.first_name} {obj.advisor.last_name}"  

admin.site.register(Appointments, CustomApoAdmin)
