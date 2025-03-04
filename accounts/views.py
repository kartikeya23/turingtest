from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			print("user logged in: ", user.username)
			return redirect('play')
		else:
			print('unknown user')
			return render(request, 'accounts/login.html', {'error': 'user not found'})
	else:
		return render(request, 'accounts/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request,)
		return redirect('login')
