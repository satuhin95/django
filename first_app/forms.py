from django import forms

class user_form(forms.Form):
    boolear_field = forms.BooleanField(required=False)
    char_field = forms.CharField(max_length=15, min_length=5)
    choices=(('','Select'),('1','First'),('2','Second'))
    choiec_field = forms.ChoiceField(choices=choices , required=False)
    radio = (('A','A'),('B','B'))
    radio_field = forms.ChoiceField(choices=radio,widget=forms.RadioSelect)
    mulchoiec_field = forms.MultipleChoiceField(choices=choices , required=False)