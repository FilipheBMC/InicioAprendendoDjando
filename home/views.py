from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    print("Minha home")
    return HttpResponse("Minha home")