from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'hello.html')

