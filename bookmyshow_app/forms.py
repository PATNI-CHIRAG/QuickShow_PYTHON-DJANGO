from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
    password = forms.CharField(widget=forms.PasswordInput)

from .models import Movie,Show
from django.forms import modelformset_factory

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'image1', 'image2', 'year', 'genre', 'time', 'rate', 'price', 'description']



class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

# Formset for multiple shows
# ShowFormSet = modelformset_factory(Show, form=ShowForm, extra=3, can_delete=True)





    
