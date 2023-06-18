from django import forms

class user_form(forms.Form):
    user_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':"Enter Your Name",'style':"width:150px"}))
    user_email = forms.EmailField(label='User Email',widget=forms.TextInput(attrs={'placeholder':"Enter Your Email"}))
    user_dob = forms.DateField(label='Date of Birth', widget=forms.TextInput(attrs={'type':'date'}))
    