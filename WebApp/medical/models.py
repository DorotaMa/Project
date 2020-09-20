from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse

PLEC_CHOICES = [('K','k'),
                ('M','m'),]


class Pacjent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    imie = models.CharField(max_length=50, blank=True, default=None)
    nazwisko = models.CharField(max_length=50)
    rok_urodzenia = models.DateTimeField(blank=True, null=True)
    plec = models.CharField(max_length=1, choices=PLEC_CHOICES)
    tel_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                               message="Proszę podać numer telefonu w formacie: +999999999.")
    numer_telefonu = models.CharField(validators=[tel_regex], max_length=17, blank=True)
    data_utworzenia_konta = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.imie}"


class Wizyta(models.Model):
    day = models.DateField("Dzień wizyty", help_text="Dzień wizyty")
    start_time = models.TimeField("Godzina rozpoczęcia wizyty", help_text="Godzina wityty")
    end_time = models.TimeField("Godzina zakończenia wizyty", help_text="Godzina zakończenia")
    notes = models.TextField("Notatki", help_text='Miejsce na Twoje notatki', blank=True)
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE, default=None, blank=True, null=True)

    class Meta:
        verbose_name = u'Kalendarz wizyt'
        verbose_name_plural = u'Kalendarz wizyt'

    def __str__(self):
        return f'{self.day} {self.start_time}'

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (
                new_end >= fixed_start and new_end <= fixed_end):  # innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
            overlap = True

        return overlap


    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        events = Wizyta.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))




# class Komentarz(models.Model):
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     email = models.EmailField
#     message = models.TextField("Wiadomość", max_length=500)
#     # patient = models.ForeignKey(Pacjent, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'Pacjent: {self.name} {self.surname} e-mail: {self.email}. Pytanie: {self.message}'

