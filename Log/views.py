from django.shortcuts import render, redirect
from .models import Log
from Meal.models import Meal
from Activity.models import Activity
from datetime import date

# Create your views here.

def list(request):
    user = request.user
    logs = Log.objects.filter(member=user).order_by('-date')

    context = {
        'logs': logs,
    }

    return render(request, 'log/list.html', context)
