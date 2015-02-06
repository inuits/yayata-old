from django.contrib import admin
from models import Customer, Project

admin.site.register(Customer, admin.ModelAdmin)
admin.site.register(Project, admin.ModelAdmin)

