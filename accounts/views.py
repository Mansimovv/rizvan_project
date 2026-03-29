
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from .models import Profile

def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password']
			)
			Profile.objects.create(
				user=user,
				full_name=form.cleaned_data['full_name'],
				email=form.cleaned_data['email']
			)
			messages.success(request, "Qeydiyyat uğurla tamamlandı! Zəhmət olmasa daxil olun.")
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password']
			)
			if user:
				login(request, user)
				messages.success(request, "Uğurla daxil oldunuz.")
				return redirect('home')
			else:
				messages.error(request, "İstifadəçi adı və ya şifrə yanlışdır.")
	else:
		form = LoginForm()
	return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
	logout(request)
	messages.info(request, "Çıxış etdiniz.")
	return redirect('login')
