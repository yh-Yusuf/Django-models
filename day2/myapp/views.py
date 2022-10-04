from django.shortcuts import render
from .models import *
from django.http import *
# Create your views here.

def index(request):
    d = Post.objects.all()

    for i in d:
        print(i.title)
        print(i.text)

    return HttpResponse("Hello !")
