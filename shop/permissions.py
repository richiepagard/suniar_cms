from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # return bool(
        #     request.user.is_superuser and
        #     request.user.is_authenticated
        #     or
        #     obj.owner == request.user
        #
        # )
        is_super = request.user.is_authenticated and request.user.is_superuser
        is_owner = request.user == obj.owner

        return is_super or is_owner
