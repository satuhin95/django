from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms
# Create your views here.


def home(request):
    musicions = Musician.objects.order_by('first_name')
    diction ={'name':"Comilla Victoria Govt College",'musicions':musicions}
    return render(request, 'first_app/index.html', context=diction)


def form(request):
   new_form = forms.user_form()
   diction = {'test_form':new_form,'heading_1':'Django Form Library'}
   if request.method  == 'POST':
       new_form = forms.user_form(request.POST)

       if new_form.is_valid():
           user_name = new_form.cleaned_data['user_name']
           user_email = new_form.cleaned_data['user_email']
           user_dob = new_form.cleaned_data['user_dob']

           diction.update({'user_name':user_name})
           diction.update({'user_email':user_email})
           diction.update({'user_dob':user_dob})
           diction.update({'form_submited':'yes'})

   return render(request, 'first_app/form.html', context=diction ) 