from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.models import User
from .models import Appointments

def appointments_list(request):
    accepted_appointments = Appointments.objects.filter(status='available').order_by('appointment_time')
    return render(request,'appointments.html', {'appointments': accepted_appointments})

@login_required
@user_passes_test(lambda u: u.role == 'admin')
def create_appointment(request):
    pass

@login_required
@user_passes_test(lambda u: u.role == 'advisor')
def update_status(request, appointment_id):
    appointment = get_object_or_404(Appointments, id=appointment_id)

    if appointment.advisor != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Appointments.STATUS):
            appointment.status = new_status
            appointment.save()
            messages.success(request, '✅ وضعیت نوبت با موفقیت بروزرسانی شد')
        else:
            messages.error(request, '❌ وضعیت نامعتبر است')
    
    return redirect('accounts:advisor_dashboard')


