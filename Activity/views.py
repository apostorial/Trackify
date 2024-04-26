from django.shortcuts import render
from .forms import ActivityForm
from .models import Activity
import requests, os
from dotenv import load_dotenv

load_dotenv()

load_dotenv()

# Create your views here.

headers = {
	"X-Api-Key": os.getenv("X-API-KEY")
}

defaultQuery = "Rock Climbing"
defaultDuration = 60

def search(request):
    query = request.POST.get('query', defaultQuery)
    duration = request.POST.get('duration', defaultDuration)
    response = requests.get(f'https://api.api-ninjas.com/v1/caloriesburned?activity={query}&duration={duration}', headers=headers)
    data = response.json()
    context = {
        'data': data,
        'defaultQuery': defaultQuery,
        'defaultDuration': defaultDuration
    }

    return render(request, 'activity/search.html', context)

def add(request):
    form = ActivityForm(request.POST)
    userActivities = Activity.objects.filter(member=request.user)
    if form.is_valid():
        date = form.cleaned_data['date']
        query = form.cleaned_data['query']
        duration = form.cleaned_data['duration']
        response = requests.get(f'https://api.api-ninjas.com/v1/caloriesburned?activity={query}&duration={duration}', headers=headers)
        data = response.json()
        context = {
                'form': form,
                'userActivities': userActivities,
                'defaultQuery': defaultQuery,
                'defaultDuration': defaultDuration
            }
        for item in data:
            activity = Activity(
                member=request.user,
                date=date,
                name=item['name'],
                caloriesPerHour=item['calories_per_hour'],
                durationMinutes=item['duration_minutes'],
                totalCalories=item['total_calories']
            )
            activity.save()
        return render(request, 'activity/add.html', context)
    else:
        context = {
            'form': form,
            'userActivities': userActivities,
            'defaultQuery': defaultQuery,
            'defaultDuration': defaultDuration
        }
        return render(request, 'activity/add.html', context)