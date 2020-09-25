from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


PLEC_CHOICES = [('k', 'K'),
                ('m', 'M'), ]


class Pacjent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    imie = models.CharField(max_length=50, default=None)
    nazwisko = models.CharField(max_length=50)
    rok_urodzenia = models.CharField(max_length=4)
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