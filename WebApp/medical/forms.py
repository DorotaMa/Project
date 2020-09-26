from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Pacjent

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class RegisterForm(UserCreationForm):
    #email = forms.EmailField()   # dodajemy swoje pole email

    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
        labels = {
            "username": "Nazwa Użytkownia",
            "email": "Email",
            "password1": "Hasło",
            "password2": "Powtórz hasło",
        }
        # jezeli chcemy dodac aliasy nalezy dodac Labels -> poczytaj jak to zrobic
        # jezeli nie ma byc napisow dot. password nalezy to usunąc z settings aplikacji passworD_validation
        # aby to ladniej wygladalo trzeba pobrac crispy
        # custom user model => dodatkowa tablea


# do podmiany adresy e-mail

class AskingQuestion(forms.Form):
    name = forms.CharField(
        max_length=15,
        label='Imię:',
        required=True,
    )

    surname = forms.CharField(
        max_length=25,
        label='Nazwisko:',
        required=True,
    )

    email = forms.EmailField(
        label='Adres e-mail:',
        required=True,
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label='Wpisz swoje pytanie tutaj:'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-askingQuestion'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'question'
        self.helper.form_style = 'default'


        self.helper.layout = Layout(
            Fieldset(
                'Formularz kontaktowy',
                'name',
                'surname',
                'email',
                'message',

            ),
            ButtonHolder(
                Submit('submit', 'Wyślij', css_class='button white')
            )
        )
    # name = forms.CharField(max_length=15, label='Imię:')
    # surname = forms.CharField(max_length=25, label='Nazwisko:')
    # email = forms.EmailField(label='Adres e-mail:')
    # message = forms.CharField(required=True, widget=forms.Textarea, label='Wpisz swoje pytanie tutaj:')


class UserDetails(ModelForm):
    class Meta:
        model = Pacjent
        fields = ['imie', 'nazwisko', 'rok_urodzenia', 'plec', 'numer_telefonu']
