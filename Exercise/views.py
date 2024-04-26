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

@login_required
def exerciseList(request, exerciseType):
    response = requests.get(f'https://exercisedb.p.rapidapi.com/exercises/{exerciseType}List', headers=headers)
    dataList = response.json()
    context = {
        'dataList': dataList,
        'exerciseType': exerciseType,
    }

    return render(request, 'exercise/exerciseList.html', context)

@login_required
def exerciseInfo(request, exerciseType, exerciseSecondaryType):
    response = requests.get(f'https://exercisedb.p.rapidapi.com/exercises/{exerciseType}/{exerciseSecondaryType}', headers=headers, params=querystring)
    dataList = response.json()
    context = {
        'dataList': dataList,
        'exerciseType': exerciseType,
        'exerciseSecondaryType': exerciseSecondaryType,
    }

    return render(request, 'exercise/exerciseInfo.html', context)