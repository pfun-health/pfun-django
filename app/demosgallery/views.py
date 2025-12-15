from django.http import HttpResponse
from django.shortcuts import render

# views for demosgallery app

def index(request):
    return HttpResponse("Welcome to the pfun demos gallery index.")
