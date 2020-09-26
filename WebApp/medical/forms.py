from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UsernameField

from .models import Pacjent


# class CustomAuthenticationForm(AuthenticationForm):
#     username = UsernameField(
#         label='Team Name',
#         widget=forms.TextInput(attrs={'autofocus': True})
#     )


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class AskingQuestion(forms.Form):
    name = forms.CharField(max_length=15)
    surname = forms.CharField(max_length=25)
    email = forms.EmailField()
    message = forms.CharField(required=True, widget=forms.Textarea)


class UserDetails(ModelForm):
    class Meta:
        model = Pacjent
        fields = ['imie', 'nazwisko', 'rok_urodzenia', 'plec', 'numer_telefonu']
