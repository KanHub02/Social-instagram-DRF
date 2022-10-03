from email import message
from lib2to3.pytree import Base
from pickle import TRUE
from rest_framework.permissions import BasePermission, SAFE_METHODS

from user_api.models import FollowerSystem, User


class CustomAuthenticatedPermission(BasePermission):
    message = "User is not authenticated or object has private status"

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and obj.is_private == False:
            return True

        elif request.user.is_authenticated and obj.is_private == True:
            return True


class UserProfilePermission(BasePermission):
    message = "User is not authenticated or this profile incorrect"

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user == obj:
            return True


class IsAnonymous(BasePermission):
    mesasge = "Allows the request only to unauthorized users"

    def has_permission(self, request, view):
        return not request.user.is_authenticated
