from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #Esta vista solo nos va a mostrar el texto de "Hello World!"

    return HttpResponse("Hello World")

def inicio(request):
    my_dict = {'insert_me': "Hello, I'm  from view.py"}
    return render(request, 'index.html', context=my_dict)
