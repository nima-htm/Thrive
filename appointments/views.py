from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import PermissionDenied

from accounts.models import User
from django.shortcuts import render
from .models import Appointments

def appointments_list(request):
    accepted_appointments = Appointments.objects.filter(status='accepted').order_by('apo_time')
    return render(request,'appointments.html', {'appointments': accepted_appointments})

@login_required
@user_passes_test(lambda u: u.role == 'admin')
def create_appointment(request):
    if not request.user.role == 'admin':
        raise PermissionDenied

    if request.method == 'POST':
        form = request.POST.
