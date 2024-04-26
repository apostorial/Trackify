from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=255)
    caloriesPerHour = models.FloatField()
    durationMinutes = models.FloatField()
    totalCalories = models.FloatField()