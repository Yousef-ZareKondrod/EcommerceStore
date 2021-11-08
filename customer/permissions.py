from rest_framework import permissions


class IsSuperUserOrOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email or request.user.is_superuser
