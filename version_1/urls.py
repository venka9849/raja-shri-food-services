from django.contrib import admin
from django.urls import path
from version_1 import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/',views.home,name="home"),
]