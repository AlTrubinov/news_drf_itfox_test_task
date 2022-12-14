from rest_framework import permissions


class IsAuthorOrAdminOrReadOnly(permissions.BasePermission):
    """Checks if the user is the author of the news/comment or an administrator,
    otherwise it prohibits editing"""

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a news or admin
        return obj.author == request.user or request.user.is_staff
