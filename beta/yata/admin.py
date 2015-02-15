from django.contrib import admin
from models import Customer, Project, Timesheet, Hour, Company, ApiStatus
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ApiInline(admin.StackedInline):
    model = ApiStatus
    can_delete = False
    verbose_name_plural = 'api status'


class UserAdmin(UserAdmin):
    inlines = (ApiInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Customer, admin.ModelAdmin)
admin.site.register(Project, admin.ModelAdmin)
admin.site.register(Timesheet, admin.ModelAdmin)
admin.site.register(Hour, admin.ModelAdmin)
admin.site.register(Company, admin.ModelAdmin)

