from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .backends import EmailBackend


from .forms import UserRegistrationForm


def user_login(request):
	if request.method == "POST":
	    email = request.POST.get('email')
	    password = request.POST.get('password')
	    user = EmailBackend.authenticate(request, username = email, password = password)
	    if user is not None:
	        login(request, user)
	       	redirect_url = request.GET.get('next', 'home:dashboard')
	       	return	redirect(redirect_url)
	    else:
	    	messages.error(request, 'Invalid credentials supplied.')
	return render(request,'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('accounts:login')

def user_registration(request):

	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = User.objects.create_user(username, email=email, password=password)
			messages.success(request, 'Thanks! You have Successfully Registered!!')
			return redirect('accounts:login')
	else:
		form = UserRegistrationForm()

	return render(request, 'register.html', {'form': form})

	       