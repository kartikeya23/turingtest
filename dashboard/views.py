from django.shortcuts import render, redirect
from django.utils import timezone
from accounts.models import School
from django.contrib.auth.models import User
from django.core import serializers
from .models import Level
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	return redirect('play')

@login_required
def play(request):
	school = request.user.school
	if school.level >= 2:
		return render(request, 'dashboard/finished.html')
	currlvl = Level.objects.get(number=school.level)
	print(currlvl)
	if request.method == "POST":
		response = request.POST['answer'].lower()
		print(f"{school.display_name} answered {response} for level {school.level}")
		if response == currlvl.answer:
			school.level += 1
			school.time = timezone.now()
			print(f"{school.school_name} is now on level {school.level} at {timezone.now()}")
			school.save()
		return redirect('play')
	return render(request,'dashboard/level.html', {'question': currlvl.question, 'number': currlvl.number})

def leaderboard(request):
	all_users = School.objects.order_by('-level', 'time')
	return render(request, 'dashboard/leaderboard.html', {'standings': all_users})
