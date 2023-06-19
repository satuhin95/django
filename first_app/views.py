from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms
from django.db.models import Avg, Max
# Create your views here.


def index(request):
    musicions = Musician.objects.order_by('first_name')
    diction ={'title':"Home Page",'musicions':musicions}
    return render(request, 'first_app/index.html', context=diction)

def album_list(request):
    albums = Album.objects.order_by('id')
    diction = {'title':'List of Album','albums':albums}
    return render(request,'first_app/album_list.html', context=diction)
def musician_details(request,id):
    musicion = Musician.objects.get(pk=id)
    albums = Album.objects.filter(artist=id)
    artist_reating = albums.aggregate(avg=Avg('num_stars'))
    diction = {'title':'Musician Details','albums':albums,'musicion':musicion,'artist_reating':artist_reating}
    return render(request,'first_app/musician_details.html', context=diction)

def musician_edit(request,id):
    musicion = Musician.objects.get(pk=id)
    form = forms.MusicianForm(instance=musicion)
    if request.method == "POST":
        form = forms.MusicianForm(request.POST, instance=musicion)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
            

    diction = {'title':'Musician Edit','edit_form':form}
    return render(request,'first_app/musician_edit.html', context=diction)

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
def album_edit(request,id):
    album = Album.objects.get(pk=id)
    form = forms.AlbumForm(instance=album)
    diction ={}
    if request.method == "POST":
        form = forms.AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'message':"Update Successfully"})


    diction.update({'title':'Edit Album','album_form':form})
    return render(request,'first_app/album_edit.html', context=diction)
def album_delete(request,id):
    album = Album.objects.get(pk=id)
    album.delete()
    return album_list(request)
def musician_delete(request,id):
    musician = Musician.objects.get(pk=id)
    musician.delete()
    return index(request)

