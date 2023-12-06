from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False


class ModelViewSetsPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["POST", "PUT", "DELETE"]:
            return False
        return True