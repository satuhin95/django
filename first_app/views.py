from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    diction ={'name':"Comilla Victoria Govt College"}

    return render(request, 'first_app/index.html', context=diction)
