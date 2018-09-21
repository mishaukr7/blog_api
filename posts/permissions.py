from rest_framework.permissions import BasePermission


class UserThemselvesPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if (obj.user == request.user) or request.user.is_staff:
            return True
        else:
            return False

