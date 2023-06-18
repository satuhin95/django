from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms
# Create your views here.


def index(request):
    musicions = Musician.objects.order_by('first_name')
    diction ={'title':"Home Page",'musicions':musicions}
    return render(request, 'first_app/index.html', context=diction)

def album_list(request):
    albums = Album.objects.order_by('id')
    diction = {'title':'List of Album','albums':albums}
    return render(request,'first_app/album_list.html', context=diction)

def musician_form(request):
    form = forms.MusicianForm()

    if request.method == "POST":
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)    

    diction = {'title':'Add Musician','musician_form':form}
    return render(request,'first_app/add_musician.html', context=diction)

def add_album(request):
    form = forms.AlbumForm()

    if request.method == "POST":
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request)


    diction = {'title':'Add Album','album_form':form}
    return render(request,'first_app/add_album.html', context=diction)

