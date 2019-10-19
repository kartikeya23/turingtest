from django.db import models

# Create your models here.
class Level(models.Model):
  question = models.TextField()
  answer = models.CharField(max_length=20)
  short_name = models.CharField(max_length=20)
  number = models.PositiveSmallIntegerField()

  def __str__(self):
  	return self.short_name