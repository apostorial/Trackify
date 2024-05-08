from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests, os
from dotenv import load_dotenv

load_dotenv()

headers = {
	"X-RapidAPI-Key": os.getenv("RAPIDAPI-KEY"),
	"X-RapidAPI-Host": os.getenv("RAPIDAPI-HOST")
}

query = {"limit":"325"}
itemsPerPage = 12

# Create your views here.

def exerciseList(request, exerciseType):
    response = requests.get(f'https://exercisedb.p.rapidapi.com/exercises/{exerciseType}List', headers=headers)
    dataList = response.json()
    context = {
        'dataList': dataList,
        'exerciseType': exerciseType,
    }

    return render(request, 'exercise/exerciseList.html', context)

def exerciseInfo(request, exerciseType, exerciseSecondaryType):
    response = requests.get(f'https://exercisedb.p.rapidapi.com/exercises/{exerciseType}/{exerciseSecondaryType}', headers=headers, params=query)
    dataList = response.json()
    paginator = Paginator(dataList, itemsPerPage)
    pageNumber = request.GET.get('page', 1)

    try:
        page = paginator.page(pageNumber)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'exerciseType': exerciseType,
        'exerciseSecondaryType': exerciseSecondaryType,
    }

    return render(request, 'exercise/exerciseInfo.html', context)