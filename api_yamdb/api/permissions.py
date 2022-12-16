from rest_framework import permissions


class AuthorAdminModeratorPermission(permissions.IsAuthenticatedOrReadOnly):
    """Изменение только авторам/админам/модераторам."""
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role in ('moderator', 'admin')
                or obj.author == request.user)


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and request.user.role == 'admin'))
