from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import Group

class Customer(models.Model):
    short_name = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    country = CountryField()

    def __unicode__(self):
        return self.name

class Project(models.Model):
    short_name = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    customer = models.ForeignKey('Customer')
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    billable = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, blank=True)

    def __unicode__(self):
        return self.name
