from django import forms
from django.core import validators
from first_app.models import Album, Musician


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields= "__all__"

