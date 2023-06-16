from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("<h1>This is home page</h1> <br><a href='contact/'> Contact</a> <br><a href='about/'> About</a>")

def contact(request):
    return HttpResponse("<h1>This is contact page</h1> <br><a href='/'> Home</a> <br><a href='/about/'> About</a>")

def about(request):
    return HttpResponse("<h1>This is about page</h1> <br><a href='/contact/'> Contact</a> <br><a href='/'> Home</a>")