from django.contrib import admin
from models import Customer, Project, Timesheet, Hour, Company

admin.site.register(Customer, admin.ModelAdmin)
admin.site.register(Project, admin.ModelAdmin)
admin.site.register(Timesheet, admin.ModelAdmin)
admin.site.register(Hour, admin.ModelAdmin)
admin.site.register(Company, admin.ModelAdmin)

