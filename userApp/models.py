from django.db import models
from django.contrib.auth.models import AbstractUser
from mainApp.models import *


class Profil(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=(('M','Male'),('F','Female')))
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL,null=True)
    birth_date = models.DateField(blank=True, null=True)



    def __str__(self):
        return self.username
