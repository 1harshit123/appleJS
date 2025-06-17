
from django.contrib import admin
from django.urls import path, include
from apple import views

urlpatterns = [
    path('', views.Checking, name='test')
]
