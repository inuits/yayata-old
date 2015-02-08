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

    def __unicode__(self):
        return "%s - %s - %s" % (self.month, unicode(self.project), unicode(self.user))

    class Meta:
        permissions = (
            ('view_all_timesheets', 'View all the timesheets'),
            ('change_timesheet_company', 'Change the company'),
            ('change_timesheet_user', 'Change the timesheet user'),
            ('change_timesheet_group', 'Change the timesheet group'),
        )

    def clean(self):
        self.month = self.month.replace(day = 1)

    def save(self, *args, **kwargs):
        self.clean()
        super(Timesheet, self).save(*args, **kwargs)


class Hour(models.Model):
    timesheet = models.ForeignKey('Timesheet')
    description = models.CharField(max_length=80, blank=True)
    hours = models.DecimalField(max_digits=4, decimal_places=2)
    day = models.DateField()

    class Meta:
        permissions = (
            ('view_hour', 'View hour'),
        )

