from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Pacjent


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
        labels = {
            "username": "Nazwa Użytkownia",
            "email": "Email",
            "password1": "Hasło",
            "password2": "Powtórz hasło",
        }


class AskingQuestion(forms.Form):
    name = forms.CharField(max_length=15)
    surname = forms.CharField(max_length=25)
    email = forms.EmailField()
    message = forms.CharField(required=True, widget=forms.Textarea)


class UserDetails(ModelForm):
    class Meta:
        model = Pacjent
        fields = ['imie', 'nazwisko', 'rok_urodzenia', 'plec', 'numer_telefonu']

