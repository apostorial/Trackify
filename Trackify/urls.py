"""
URL configuration for Trackify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('member/', include('django.contrib.auth.urls')),
    path('member/', include('Member.urls')),
    path('member/', include('MemberInfo.urls')),
    path('exercises/', views.exercise, name='exercise'),
    path('exercises/body_part_list', views.body_part_list, name='body_part_list'),
    path('exercises/equipment_list', views.equipment_list, name='equipment_list'),
    path('exercises/target_list', views.target_list, name='target_list'),
    path('exercises/body_part/<str:body_part>/', views.body_part_info, name='body_part_info'),
    path('exercises/equipment/<str:equipment>/', views.equipment_info, name='equipment_info'),
    path('exercises/target/<str:target>/', views.target_info, name='target_info'),
    path('food/', views.food, name='food'),
    path('food/search', views.search, name='search'),
]
