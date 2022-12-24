from rest_framework import permissions


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated
                and request.user.role == 'admin'
                or request.user.is_staff
                or request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        return request.method in ('GET', 'POST', 'PATCH', 'DELETE')
