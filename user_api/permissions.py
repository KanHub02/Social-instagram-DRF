from lib2to3.pytree import Base
from pickle import TRUE
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticated(BasePermission):
    message = "Please authorize to have permission"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True


class HavePermissionForNotSafeMethods(BasePermission):
    message = "User has not permission for change data"

    def has_object_permission(self, request, view, obj):
        if (
            request.method not in SAFE_METHODS
            and request.user != obj
            and not request.user.is_authenticated
        ):
            return False


class IsTrueUser(BasePermission):
    message = "User incorrect"

    def has_object_permission(self, request, view, obj):
        if request.user.is_autheticated and request.method in SAFE_METHODS:
            return True