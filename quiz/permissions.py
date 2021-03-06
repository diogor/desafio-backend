from rest_framework import permissions
from users.models import User


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return (request.user.type == User.ADMIN
                or request.user.is_superuser)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return ((request.user.type == User.ADMIN or request.user.is_superuser)
                or (request.method in permissions.SAFE_METHODS
                    and request.user.type == User.PLAYER))
