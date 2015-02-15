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
        if user.is_staff or obj.user == user:
            return True
        return False
