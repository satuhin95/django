from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm, UserProfileChange ,ProfilePicture
# Create your views here.


def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            form.save(commit=True)
            registered = True
    dict = {'form':form, 'registered':registered}
    return render(request, 'App_Login/sign_up.html',context=dict) 

def login_page(request):
    form = AuthenticationForm()
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_Login/login.html', context={'form':form})        

@login_required           
def logout_user(request):
    logout(request)     
    return HttpResponseRedirect(reverse('index'))

@login_required
def user_profile(request):
    return render(request, 'App_Login/profile.html', context={})  
@login_required
def user_change(request):  
    current_user =  request.user
    form = UserProfileChange(instance=current_user)   
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = UserCreationForm(instance=current_user)
    return render(request, 'App_Login/change_profile.html', context={'form':form})  

@login_required
def password_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method =='POST':
        form = PasswordChangeForm(current_user, data = request.POST)
        if form.is_valid():
            form.save() 
            changed= True
    return render(request, 'App_Login/password_change.html', context={'form':form,'changed':changed})        
@login_required
def profile_change(request):
    form = ProfilePicture()
    if request.method == 'POST':
        form = ProfilePicture(request.POST, request.FILES)
        if form.is_valid():
            userObj = form.save(commit=False)
            userObj.user = request.user
            userObj.save()
            return HttpResponseRedirect(reverse('App_Login:user_profile'))


    return render(request, 'App_Login/profile_picture.html' , context={'form':form})

@login_required
def change_profile_pic(request):
    form  = ProfilePicture(instance=request.user.user_profile)
    if request.method == 'POST':
       form = ProfilePicture(request.POST, request.FILES, instance=request.user.user_profile)
       if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:user_profile'))

    return render(request, 'App_Login/profile_picture.html' , context={'form':form})