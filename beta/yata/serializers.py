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

