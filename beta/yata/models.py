from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import Group, User

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
    #start_date = models.DateField(blank=True,null=True)
    #end_date = models.DateField(blank=True,null=True)
    #billable = models.BooleanField(default=True)
    #groups = models.ManyToManyField(Group, blank=True)

    def __unicode__(self):
        return self.name

class Company(models.Model):
    ''' The companies that will make invoices '''
    name = models.CharField(max_length=30)

class Timesheet():
    month = models.DateField()
    project = models.ForeignKey('Project')
    company = models.ForeignKey('Company')
    group = models.ForeignKey('Group')
    user = models.ForeignKey('User')

    class Meta():
        permissions = (
            ('view_timesheet', 'View timesheet'),
            ('change_timesheet_company', 'Change the company'),
            ('change_timesheet_user', 'Change the timesheet user'),
            ('change_timesheet_group', 'Change the timesheet group'),
        )

class Hour():
    timesheet = models.ManyToManyField('Timesheet')
    description = models.CharField(max_length=80, blank=True)
    hours = models.DecimalField(max_digits=4, decimal_places=2)
    day = models.DateField()

    class Meta():
        permissions = (
            ('view_hour', 'View hour'),
        )

