from rest_framework import permissions


class AuthorAdminModeratorPermission(permissions.BasePermission):
    """Изменение только авторам/админам/модераторам."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role in ('moderator', 'admin'):
            return True
        return obj.author == request.user


class AdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated:
            if request.user.role in ('admin'):
                return True
        return False
