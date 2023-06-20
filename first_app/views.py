from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView ,ListView , DetailView,CreateView,UpdateView,DeleteView
from first_app.models import Musician ,Album
from django.urls import reverse_lazy

class IndexView(ListView):
    context_object_name = 'musician_list'
    model = Musician
    template_name = 'first_app/index.html'

class MusicianDetails(DetailView):
    context_object_name = 'musician'
    model = Musician
    template_name ='first_app/musician_details.html'

class MusicianCreate(CreateView):
    fields = ('first_name','last_name','instrument')
    model = Musician
    template_name = 'first_app/add_musician.html' 

class MusicianUpdate(UpdateView):
    fields = ('first_name','last_name','instrument')   
    model = Musician
    template_name = 'first_app/musician_edit.html' 

class MusicianDelete(DeleteView):
    context_object_name = 'musician'
    model = Musician
    success_url = reverse_lazy('first_app:index')
    template_name = 'first_app/musician_delete.html' 

