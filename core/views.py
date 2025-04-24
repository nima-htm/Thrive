from django.shortcuts import render
from appointments.models import Appointments
from accounts.models import User


def home(request):
    return render(request,'home.html')

def advisor_list(request):
    advisors = User.objects.filter(role='advisor').order_by('date_joined')
    return render(request, 'advisor_list.html', {'advisors' : advisors})