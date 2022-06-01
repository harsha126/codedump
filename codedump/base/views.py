from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home")

def rooms(request):
    return HttpResponse("rooms")