from rest_framework import permissions


class AuthorAdminModeratorPermission(permissions.BasePermission):
    """Изменение только авторам/админам/модераторам."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
