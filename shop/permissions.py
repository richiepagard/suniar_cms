from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Define Permission for Crud if user is owner else just can read. """

    def has_object_permission(self, request, view, obj):
        """ every one has permission to read it."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
