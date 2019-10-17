from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
	school_name = models.CharField(max_length=40)
	display_name = models.CharField(max_length=15)
	level = models.IntegerField(default=0)
	login = models.OneToOneField(User, on_delete=models.CASCADE)