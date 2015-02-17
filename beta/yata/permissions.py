from rest_framework.permissions import SAFE_METHODS
from models import Timesheet

class OwnerOrAdminPermission:
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated():
            return False
        return True
    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user or not user.is_authenticated():
            return False
        if user.is_staff or (obj.user == user and not obj.locked):
            return True
        if obj.user == user and request.method in SAFE_METHODS:
            return True
        return False

class OwnerOrAdminHourPermission:
    def has_permission(self, request, view):
        user = request.user
        timesheet_obj = Timesheet.objects.get(id=int(request.parser_context['kwargs']['timesheet_pk']))
        if not user or not user.is_authenticated():
            return False
        if user.is_staff or (timesheet_obj.user == user and not timesheet_obj.locked):
            return True
        if timesheet_obj.user == user and request.method in SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        timesheet_obj = Timesheet.objects.get(id=int(request.parser_context['kwargs']['timesheet_pk']))
        if not user or not user.is_authenticated():
            return False
        if user.is_staff or (timesheet_obj.user == user and not timesheet_obj.locked):
            return True
        if timesheet_obj.user == user and request.method in SAFE_METHODS:
            return True
        return False
