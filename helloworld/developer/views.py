from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def respond(request):
    name = request.GET.get('name','')
    return HttpResponse("Hello "+name)
