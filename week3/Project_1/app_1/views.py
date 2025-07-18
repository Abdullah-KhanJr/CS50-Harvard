from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, World!") 

def abdullah(request):
    return HttpResponse("Hello, Abdullah")

def another_function(request):
    return HttpResponse("Hello , Somebody")

def greet(request, name, gender, age):
    return HttpResponse(f"Hello, {name.capitalize()}, you are a {gender} and your age is {age}.")

def index(request):
    return render(request, "app/index.html")