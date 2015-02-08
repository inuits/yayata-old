from django.test import TestCase
from yata.models import Timesheet, Project, Company, Customer
from datetime import date
from django.contrib.auth.models import User

class TimesheetTestCase(TestCase):
    def setUp(self):
        company = Company.objects.create(name="Inuits")
        customer = Customer.objects.create(short_name="ESQ", name="Esquimaux")
        project = Project.objects.create(name="Project X", short_name="PX", customer=customer)
        user = User.objects.create(username="tux")
        Timesheet.objects.create(user=user, project=project, month=date(2015,01,01), company=company)

    def test_timesheet_month_first_day(self):
        """Check that when changing the date it is set to the 1st of the month """
        ts = Timesheet.objects.get(id=1)
        ts.month = date(2015,01,02)
        ts.save()
        ts = Timesheet.objects.get(id=1)
        self.assertEqual(ts.month, date(2015,01,01))
        ts.month = date(2015,05,01)
        ts.save()
        ts = Timesheet.objects.get(id=1)
        self.assertEqual(ts.month, date(2015,05,01))
        ts.month = date(2015,02,06)
        ts.save()
        ts = Timesheet.objects.get(id=1)
        self.assertEqual(ts.month, date(2015,02,01))



