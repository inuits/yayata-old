from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError

class Customer(models.Model):
    short_name = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    country = CountryField()

    class Meta:
        permissions = (
            ('api_read_only', 'Read-Only full API access'),
        )

    def __unicode__(self):
        return self.name

class Project(models.Model):
    short_name = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    customer = models.ForeignKey('Customer')

    class Meta:
        permissions = (
            ('api_read_only', 'Read-Only full API access'),
        )

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.customer.name)

class Company(models.Model):
    ''' The companies that will make invoices '''
    name = models.CharField(max_length=30)

    class Meta:
        permissions = (
            ('api_read_only', 'Read-Only full API access'),
        )

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
            ('api_read_only', 'Read-Only full API access'),
        )

    def clean(self):
        self.month = self.month.replace(day = 1)
        if self.user == self.group == None:
            raise ValidationError('A user or a group has to be chosed for this timesheet')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Timesheet, self).save(*args, **kwargs)


class Hour(models.Model):
    timesheet = models.ForeignKey('Timesheet')
    description = models.CharField(max_length=80, blank=True)
    hours = models.DecimalField(max_digits=4, decimal_places=2)
    day = models.DateField()

    class Meta:
        permissions = (
            ('api_read_only', 'Read-Only full API access'),
        )

