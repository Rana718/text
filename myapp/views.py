from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("Contact page")

def products(request):
    return HttpResponse("Products page")

