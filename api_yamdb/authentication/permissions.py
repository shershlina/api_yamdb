from rest_framework import permissions

from .models import UserRole


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return ((request.user.is_authenticated
                and (request.user.role == UserRole.ADMIN))
                or request.user.is_superuser)
