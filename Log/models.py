from django.db import models
from django.contrib.auth.models import User
from Meal.models import Meal
from Activity.models import Activity
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Log(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    caloriesConsumed = models.FloatField(default=0)
    caloriesBurned = models.FloatField(default=0)
    proteinsConsumed = models.FloatField(default=0)

@receiver(post_save, sender=Meal)
def updateLogOnMealCreate(sender, instance, created, **kwargs):
    if created:
        user = instance.member
        today = date.today()
        try:
            log = Log.objects.get(member=user, date=today)
            log.caloriesConsumed += instance.calories
            log.proteinsConsumed += instance.protein
            log.save()
        except Log.DoesNotExist:
            Log.objects.create(
                member=user,
                date=today,
                caloriesConsumed=instance.calories,
                proteinsConsumed=instance.protein,
            )

@receiver(post_save, sender=Activity)
def updateLogOnActivityCreate(sender, instance, created, **kwargs):
    if created:
        user = instance.member
        today = date.today()
        try:
            log = Log.objects.get(member=user, date=today)
            log.caloriesBurned += instance.totalCalories
            log.save()
        except Log.DoesNotExist:
            Log.objects.create(
                member=user,
                date=today,
                caloriesBurned=instance.totalCalories,
            )