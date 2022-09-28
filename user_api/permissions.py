from lib2to3.pytree import Base
from pickle import TRUE
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserProfilePermission(BasePermission):
    message = "User is not authenticated or this profile incorrect"

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user == obj:
            return True
