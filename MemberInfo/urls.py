from django.urls import path
from . import views

urlpatterns = [
    path('add_member_info', views.add_member_info, name='add_member_info'),
    path('stats', views.stats, name='stats'),
]
