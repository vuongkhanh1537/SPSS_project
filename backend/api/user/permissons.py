from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the owner of an object to view or edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Allow read-only methods (GET, HEAD, OPTIONS)
            return True
        # Check if the user is trying to access their own profile when performing other actions
        return obj.user_id == request.user
