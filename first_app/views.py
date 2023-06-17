from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
# Create your views here.


def home(request):
    musicions = Musician.objects.order_by('first_name')
    diction ={'name':"Comilla Victoria Govt College",'musicions':musicions}
    return render(request, 'first_app/index.html', context=diction)
