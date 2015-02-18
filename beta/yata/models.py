from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError

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

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.customer.name)

class Company(models.Model):
    ''' The companies that will make invoices '''
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Timesheet(models.Model):
    month = models.DateField()
    project = models.ForeignKey('Project')
    company = models.ForeignKey('Company')
    group = models.ForeignKey(Group,blank=True,null=True)
    user = models.ForeignKey(User,blank=True,null=True)
    locked = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s - %s - %s" % (self.month, unicode(self.project), unicode(self.user))

    def clean(self):
        self.month = self.month.replace(day = 1)
        if self.user == self.group == None:
            raise ValidationError('A user or a group has to be chosed for this timesheet')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Timesheet, self).save(*args, **kwargs)

class Hour(models.Model):
    timesheet = models.ForeignKey('Timesheet')
    task = models.CharField(max_length=80, blank=True)
    hours = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    hours150 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    hours200 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    hourstravel = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    day = models.IntegerField()
    mistaken = models.BooleanField(default=False)

    def clean(self):
        if self.day > 31 or self.day < 1:
            self.day = 1
            self.mistaken = True

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Hour, self).save(*args, **kwargs)

