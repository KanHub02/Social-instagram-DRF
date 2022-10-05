from doctest import FAIL_FAST
from email import message
from rest_framework.permissions import BasePermission, SAFE_METHODS

from user_api.models import FollowerSystem, User


class IfPostFromUserPermission(BasePermission):
    message = "This user has not permission to update or delete post!"

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and obj.author == request.user:
            return True

        else:
            return False
