from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import LoginForm, SignUpForm, AdminUserEditForm, UserProfileForm
from django.utils import timezone
from datetime import datetime, timedelta
from appointments.models import Appointments
from django.db import IntegrityError

# Create your views here.
def advisor_list(request):
    return render(request,'advisor_list.html')

def user_sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'patient'
            user.save()
            login(request, user)
            messages.success(request, ' ✅ حساب با موفقیت ایجاد شد')
            return redirect('accounts:dashboard')
        else:
            if 'username' in form.errors:
                form.errors['username'] = ['این نام کاربری قبلاً ثبت شده است. ']
 
            messages.error(request, '❌ لطفا خطاهای فرم را بررسی کنید')
            return render(request, 'accounts/signup.html', {'form': form})
           
    else:
        form = SignUpForm()
    return render(request,'accounts/signup.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Ensure you return a redirect or HttpResponse here.
            else:
                form.add_error(None, "کاربری یافت نشد")
        # Even if the form is invalid or authentication fails, you must return a response.
        return render(request, 'accounts/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ' ✅ پروفایل با موفقیت بروزرسانی شد')
            return redirect('accounts:dashboard')
        else:
            if 'username' in form.errors:
                form.errors['username'] = ['']
                messages.error(request, '❌ این نام کاربری قبلاً ثبت شده است. ')

            return render(request, 'accounts/dashboard.html', {'form': form})
    else:
        form = UserProfileForm(instance=request.user)
        return render(request, 'accounts/dashboard.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
@user_passes_test(lambda u: u.role == 'advisor')
def advisor_dashboard(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ' ✅ پروفایل با موفقیت بروزرسانی شد')
            return redirect('accounts:dashboard')
    else:
        form = UserProfileForm(instance=request.user)

    appointments = Appointments.objects.filter(advisor=request.user).order_by('appointment_time')
    
    # Update expired appointments
    current_time = timezone.now()
    expired_appointments = appointments.filter(
        appointment_time__lt=current_time,
        status='available'
    )
    expired_appointments.update(status='not_available')

    today = timezone.now().date()
    today_appointments_count = appointments.filter(appointment_time__date=today, status='available').count()
    pending_appointments_count = appointments.filter(status='pending').count()
    total_patients_count = appointments.values('patient').distinct().count() if appointments.values('patient') != "" else 0
    
    context = {
        'form': form,
        'appointments': appointments,
        'today_appointments_count': today_appointments_count,
        'pending_appointments_count': pending_appointments_count,
        'total_patients_count': total_patients_count
    }
    
    return render(request, 'advisor/advisor_dashboard.html', context)
