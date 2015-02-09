from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Customer, Project, Timesheet, Hour, Company

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('short_name', 'name', 'country')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('short_name', 'name', 'customer')

class TimesheetSerializer(serializers.ModelSerializer):
    def is_valid(self, *args, **kwargs):
        is_valid = super(TimesheetSerializer, self).is_valid(*args, **kwargs)
        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )
        if validated_data['user'] == validated_data['group'] == None:
            raise(serializers.ValidationError('You must set a user or a group'))
        return is_valid

    class Meta:
        model = Timesheet
        fields = ('month','project','company','group','user')

class HourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hour
        fields = ('timesheet', 'description', 'hours', 'day')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)

