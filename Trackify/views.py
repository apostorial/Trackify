from django.shortcuts import render
import requests

headers = {
	"X-RapidAPI-Key": "3134faf04amsh387f721f075fa27p150e4ejsn3bbafdb0a371",
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

# Create your views here.

def home(request):
    return render(request, 'index.html', {}) 

def body_part_list(request):
    response = requests.get('https://exercisedb.p.rapidapi.com/exercises/bodyPartList', headers=headers)
    body_parts = response.json()

    return render(request, 'exercise/body_part_list.html', {'body_parts': body_parts})

def equipment_list(request):
    response = requests.get('https://exercisedb.p.rapidapi.com/exercises/equipmentList', headers=headers)
    equipments = response.json()

    return render(request, 'equipment/equipment_list.html', {'equipments': equipments})

def target_list(request):
    response = requests.get('https://exercisedb.p.rapidapi.com/exercises/targetList', headers=headers)
    targets = response.json()

    return render(request, 'target/target_list.html', {'targets': targets})