from django.shortcuts import render
from .forms import MealForm
from .models import Meal
import requests, os
from dotenv import load_dotenv

load_dotenv()

headers = {
	"X-Api-Key": os.getenv("X-API-KEY")
}

defaultQuery = "Pepperoni Pizza"

def search(request):
	query = request.POST.get('query', defaultQuery)
	response = requests.get(f'https://api.api-ninjas.com/v1/nutrition?query={query}', headers=headers)
	data = response.json()
	context = {
		'data': data,
		'defaultQuery': defaultQuery
	}

	return render(request, 'meal/search.html', context)

def add(request):
    form = MealForm(request.POST)
    userMeals = Meal.objects.filter(member=request.user)
    if form.is_valid():
        date = form.cleaned_data['date']
        query = form.cleaned_data['query']
        response = requests.get(f'https://api.api-ninjas.com/v1/nutrition?query={query}', headers=headers)
        data = response.json()
        for item in data:
            meal = Meal(
                member=request.user,
                date=date,
                name=item['name'],
                calories=item['calories'],
                servingSize=item['serving_size_g'],
                totalFat=item['fat_total_g'],
                saturatedFat=item['fat_saturated_g'],
                protein=item['protein_g'],
                sodium=item['sodium_mg'],
                potassium=item['potassium_mg'],
                cholesterol=item['cholesterol_mg'],
                totalCarbohydrates=item['carbohydrates_total_g'],
                fiber=item['fiber_g'],
                sugar=item['sugar_g']
            )
            meal.save()
            context = {
                'data': data,
                'query': query,
                'form': form,
                'userMeals': userMeals
            }
        return render(request, 'meal/add.html', context)
    else:
        context = {
            'form': form,
            'userMeals': userMeals
        }
        return render(request, 'meal/add.html', context)