from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello (request):   
        return render (request, 'hello.html', {'name': 'Suhail'})

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}