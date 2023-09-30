from rest_framework import permissions

class IsSupplierPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.user_type == "supplier"
