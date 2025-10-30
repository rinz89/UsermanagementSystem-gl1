from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import *



def reg(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        em = request.POST.get('email')
        pw = request.POST.get('password')

        
        if User.objects.filter(username=un).exists():
            messages.error(request, "Username already exists. Please choose another one.")
            return render(request, 'users/register.html')

       
        if User.objects.filter(email=em).exists():
            messages.error(request, "Email already registered. Try logging in instead.")
            return render(request, 'users/register.html')

       
        try:
            user = User.objects.create_user(username=un, email=em, password=pw)
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred while creating the user: {str(e)}")
            return render(request, 'users/register.html')
       

    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')

@login_required
def profile_view(request):
    """Create user profile"""
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')

        
        if Profile.objects.filter(user=request.user).exists():
            messages.warning(request, "Profile already exists. You can update it instead.")
            return redirect('update')

        Profile.objects.create(
            user=request.user,
            full_name=full_name,
            date_of_birth=date_of_birth,
            email=email,
            address=address,
            gender=gender,
            mobile_number=mobile_number,
        )

        messages.success(request, "Profile created successfully!")
        return redirect('list')

    return render(request, 'users/profile.html')









@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'users/list.html', {'profile': profiles})



@login_required
def update_profile(request, id):
    profile = Profile.objects.get(id=id)
    if request.method == 'POST':
        profile.name = request.POST.get('name')
        profile.address = request.POST.get('address')
        profile.save()
        return redirect('list')
    return render(request, 'users/update.html', {'profile': profile})



@login_required
def reset_password(request):
    """Reset password"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in
            messages.success(request, "Password changed successfully.")
            return redirect('profile_view')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'reset_password.html', {'form': form})



 


def logout_view(request):
    response = redirect('login')
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    messages.success(request, "You have been logged out successfully.")
    return response
