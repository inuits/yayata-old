from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from yata.models import Timesheet, Project, Company, Customer
from datetime import date
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse


class YataTest(APITestCase):
    def generate_timesheet(self,name):
        company = Company.objects.create(name="%s Int" % name.title())
        customer = Customer.objects.create(short_name=name[0:3].upper(), name="Customer %s" % name.title())
        project = Project.objects.create(name="Project %s" % name.title(), short_name="P%s" % name[0:2].upper(), customer=customer)
        user = User.objects.create(username="%s_user" % name)
        return Timesheet.objects.create(user=user, project=project, month=date(2015,01,01), company=company)


class TimesheetTestCase(YataTest):
    def setUp(self):
        company = Company.objects.create(name="Inuits")
        customer = Customer.objects.create(short_name="ESQ", name="Esquimaux")
        project = Project.objects.create(name="Project X", short_name="PX", customer=customer)
        user = User.objects.create(username="tux")
        Timesheet.objects.create(user=user, project=project, month=date(2015,01,01), company=company)

    def test_timesheet_month_first_day_january(self):
        '''Check that when changing the date it is set to the 1st of the month'''
        ts = Timesheet.objects.get(id=1)
        ts.month = date(2015,01,02)
        ts.save()
        self.assertEqual(ts.month, date(2015,01,01))

    def test_timesheet_month_first_day_may(self):
        '''This time the date should not be changed'''
        ts = Timesheet.objects.get(id=1)
        ts.month = date(2015,05,01)
        ts.save()
        self.assertEqual(ts.month, date(2015,05,01))

    def test_timesheet_month_first_day_no_change_to_date(self):
        '''Another test with february'''
        ts = Timesheet.objects.get(id=1)
        ts.month = date(2015,02,06)
        ts.save()
        self.assertEqual(ts.month, date(2015,02,01))

class ACLTimesheetTestCase(YataTest):
    def setUp(self):
        self.total_timesheet = 4
        self.ts1 = self.generate_timesheet('zeus')
        self.ts2 = self.generate_timesheet('appollo')
        self.ts3 = self.generate_timesheet('artemis')
        self.ts4 = self.generate_timesheet('ares')

        content_type = ContentType.objects.get_for_model(Timesheet)
        self.view_all_acl_permission = Permission.objects.get(content_type=content_type, codename='view_all_timesheets')

        self.ts1.user.user_permissions.add(self.view_all_acl_permission)

    def test_all_acl_permission(self):
        '''test that ts1 user see both timesheets'''
        self.client.force_authenticate(user=self.ts1.user)
        url = reverse('timesheet-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.total_timesheet)

    def test_no_all_acl_permission(self):
        '''test that ts2 user see only his own timesheet'''
        self.client.force_authenticate(user=self.ts2.user)
        url = reverse('timesheet-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_anonymous_permission(self):
        '''test that anonymous user see no timesheet'''
        self.client.force_authenticate()
        url = reverse('timesheet-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

