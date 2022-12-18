from rest_framework import permissions
from authentication.models import UserRole


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return ReadOnly.has_permission(self, request, view)


class AdminOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.role == UserRole.ADMIN)

    def has_object_permission(self, request, view, obj):
        return AdminOnly.has_permission(self, request, view)


class ModeratorOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.role == UserRole.MODERATOR)

    def has_object_permission(self, request, view, obj):
        return ModeratorOnly.has_permission(self, request, view)


class AuthorOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
