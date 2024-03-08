from django.http import response
from django.shortcuts import render


# Create your views here.
# view function which only returns a string
def hello(request):
    return response.HttpResponse("Hello, Django!")
