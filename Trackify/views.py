from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests, os
from dotenv import load_dotenv

load_dotenv()

headers = {
	"X-RapidAPI-Key": os.getenv("RAPIDAPI-KEY"),
	"X-RapidAPI-Host": os.getenv("RAPIDAPI-HOST")
}
querystring = {"limit":"27"}

# Create your views here.

def home(request):
    return render(request, 'index.html', {}) 

@login_required
def exercise(request):
    response = requests.get(f'https://exercisedb.p.rapidapi.com/exercises', headers=headers)
    exercises = response.json()

    return render(request, 'exercises/exercises.html', {'exercises': exercises})

@login_required
def body_part_list(request):
    response = requests.get('https://exercisedb.p.rapidapi.com/exercises/bodyPartList', headers=headers)
    body_parts = response.json()

    return render(request, 'exercises/body_part_list.html', {'body_parts': body_parts})

@login_required
def equipment_list(request):
    response = requests.get('https://exercisedb.p.rapidapi.com/exercises/equipmentList', headers=headers)
    equipments = response.json()

    return render(request, 'exercises/equipment_list.html', {'equipments': equipments})

@login_required
def target_list(request):
    response = requests.get('https://exercisedb.p.rapidapi.com/exercises/targetList', headers=headers)
    targets = response.json()

    return render(request, 'exercises/target_list.html', {'targets': targets})

@login_required
def body_part_info(request, body_part):
    response = requests.get(f'https://exercisedb.p.rapidapi.com/exercises/bodyPart/{body_part}', headers=headers, params=querystring)
    exercises = response.json()

    return render(request, 'exercises/body_part_info.html', {'exercises': exercises})

@login_required
def equipment_info(request, equipment):
    response = requests.get(f'https://exercisedb.p.rapidapi.com/exercises/equipment/{equipment}', headers=headers, params=querystring)
    equipments = response.json()

    return render(request, 'exercises/equipment_info.html', {'equipments': equipments})

@login_required
def target_info(request, target):
    response = requests.get(f'https://exercisedb.p.rapidapi.com/exercises/target/{target}', headers=headers, params=querystring)
    targets = response.json()

    return render(request, 'exercises/target_info.html', {'targets': targets})

@login_required
def search(request):
    query = request.GET.get('query', '')
    if query:
        response = requests.get(
            f'https://api.api-ninjas.com/v1/nutrition?query={query}'
        )
        data = response.json()
        search_results = data.get('hits', [])
    else:
        search_results = []
    return render(request, 'food/food.html', {'query': query, 'search_results': search_results})

@login_required
def food(request):
    query = '1lb brisket and fries'
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={query}'
    response = requests.get(api_url, headers={'X-Api-Key': '82Ah3c9bIQ4sLJwjwp/CsQ==EmOhwj524ksVVjOc'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    return render(request, 'food/food.html')