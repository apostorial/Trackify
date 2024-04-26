from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests, os
from dotenv import load_dotenv

load_dotenv()

headers = {
	"X-Api-Key": os.getenv("X-API-KEY")
}

defaultQuery = "Rock Climbing"

def search(request):
	query = request.POST.get('query', defaultQuery)
	url = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'.format(query)
	response = requests.get(url, headers=headers)
	data = response.json()
	context = {
		'data': data,
		'defaultQuery': defaultQuery
	}

	return render(request, 'calories/search.html', context)