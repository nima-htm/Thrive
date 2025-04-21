from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from .forms import LoginForm, SignUpForm, AdminUserEditForm


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
            return redirect('home')
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


def dashboard(request):
    return None


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')