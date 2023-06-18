from django import forms
from django.core import validators
from first_app.models import Album, Musician


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields= "__all__"
        # exclude = ['first_name']
        # fields= ('first_name','last_name',)

class AlbumForm(forms.ModelForm):
    # release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Album
        fields= "__all__"
        widgets = {
            'release_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control', 'style':'width:30%'}
            )
        }

