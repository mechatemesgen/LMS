from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import CustomUser


@login_required
def dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'dashboard.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Perform user registration logic here
            # For example:
            # user = User.objects.create_user(username, email, password)
            # user.save()
            return render(request, 'registration_success.html', {'username': username})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    return render(request, 'index.html')


def user_logout(request):
    logout(request)
    # Redirect to the index page after logout
    return redirect('main:index')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_admin:
                login(request, user)
                return redirect('admin_dashboard')  # Redirect admin to admin dashboard
            elif user.is_student:
                login(request, user)
                return redirect('student_dashboard')  # Redirect student to student dashboard
            else:
                # Handle other types of users (if any)
                pass
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

from django.shortcuts import render

def admin_dashboard(request):
    # Add your view logic here
    return render(request, 'admin_dashboard.html')
