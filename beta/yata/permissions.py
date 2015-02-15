class TimesheetPermission():

    def has_permission(self, request, view):
        print 'has_permission'
        return True
    def has_object_permission(self, request, view, obj):
        print 'has_object.permission'
        return True
