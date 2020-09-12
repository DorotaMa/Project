from django.db import models
from django.urls import reverse


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)
    phone = models.IntegerField(max_length=20)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.gender}, {self.age}, {self.phone}, {self.city})"

    # def get_absolute_url(self):
    #     return reverse('views:hello')
    #
