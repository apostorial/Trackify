from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meal(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=255)
    calories = models.FloatField()
    servingSize = models.FloatField()
    totalFat = models.FloatField()
    saturatedFat = models.FloatField()
    protein = models.FloatField()
    sodium = models.FloatField()
    potassium = models.FloatField()
    cholesterol = models.FloatField()
    totalCarbohydrates = models.FloatField()
    fiber = models.FloatField()
    sugar = models.FloatField()