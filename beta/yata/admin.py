from django.contrib import admin
from models import Customer, Project, Timesheet, Hour, Company
from guardian.admin import GuardedModelAdmin

admin.site.register(Customer, GuardedModelAdmin)
admin.site.register(Project, GuardedModelAdmin)
admin.site.register(Timesheet, GuardedModelAdmin)
admin.site.register(Hour, GuardedModelAdmin)
admin.site.register(Company, GuardedModelAdmin)

