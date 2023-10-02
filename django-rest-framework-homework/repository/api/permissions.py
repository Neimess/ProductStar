from rest_framework import permissions


class IsSupplierPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Allow safe methods (e.g., GET) for all users
            return True
        if request.user.is_authenticated:
            # Check the user's user_type if they are authenticated
            return request.user.user_type == "supplier"
        return False


class IsConsumerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Allow safe methods (e.g., GET) for all users
            return True
        if request.user.is_authenticated:
            # Check the user's user_type if they are authenticated
            return request.user.user_type == "consumer"
        return False
