from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("<p>This is my first Django. </p>")
    return response
