from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, CustomerSerializer, ProjectSerializer, CompanySerializer, TimesheetSerializer, HourSerializer
from models import Customer, Project, Timesheet, Hour, Company



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class TimesheetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows timesheets to be viewed or edited.
    """
    serializer_class = TimesheetSerializer

    def get_queryset(self):
        queryset = Timesheet.objects.all()
        return queryset


class HourViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hours to be viewed or edited.
    """
    queryset = Hour.objects.all()
    serializer_class = HourSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customer to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

