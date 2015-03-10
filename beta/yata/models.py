from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
import calendar

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
    MONTH_CHOICES=[(x, calendar.month_name[x]) for x in xrange(1,12)]
    month = models.IntegerField(choices=MONTH_CHOICES)
    year = models.IntegerField()
    project = models.ForeignKey('Project')
    company = models.ForeignKey('Company')
    group = models.ForeignKey(Group,blank=True,null=True)
    user = models.ForeignKey(User,blank=True,null=True)
    locked = models.BooleanField(default=False)

    def first_day(self):
        return calendar.weekday(self.year,self.month,1)

    def max_days(self):
        return calendar.monthrange(self.year,self.month)[1]

    def __unicode__(self):
        return "%s - %s - %s" % (self.month, unicode(self.project), unicode(self.user))

    def clean(self):
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
        if self.day > self.timesheet.max_days() or self.day < 1:
            self.day = 1
            self.mistaken = True

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Hour, self).save(*args, **kwargs)

