from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Archit Shah")

def home(request):
	return render(request,"Boot_app/home.html")
