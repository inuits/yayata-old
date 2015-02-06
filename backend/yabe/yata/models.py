from django.db import models
from django_countries.fields import CountryField

class Customer(models.Model):
    short_name = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    country = CountryField()
