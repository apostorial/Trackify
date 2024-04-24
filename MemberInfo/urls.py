from django.urls import path
from . import views

urlpatterns = [
    path('add_info', views.add_info, name='add_info'),
    path('stats', views.stats, name='stats'),
]
