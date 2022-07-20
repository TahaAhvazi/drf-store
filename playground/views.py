from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# ،Takes a request -> Return a HTTP response /request Handler

def sayHello(request):
    return HttpResponse('Hello world')
