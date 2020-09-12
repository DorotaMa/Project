from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()   # dodajemy swoje pole email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Imię",
            "email": "Email",
            "password1": "Haslo",
            "password2": "Powtorz haslo",
        }
        # jezeli chcemy dodac aliasy nalezy dodac Labels -> poczytaj jak to zrobic
        # jezeli nie ma byc napisow dot. password nalezy to usunąc z settings aplikacji passworD_validation
        # aby to ladniej wygladalo trzeba pobrac crispy
        # custom user model => dodatkowa tablea