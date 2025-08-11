# CookingWeb/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my recipe vault!")

def about(request):
    return HttpResponse("My name is Weronika Górak and I want to put all the recipes I enjoy cooking in one place.")
