from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserRegisterApiView, LoginApiView, ProfileListApiView


urlpatterns = [
    path("register/", UserRegisterApiView.as_view(), name="register_api"),
    path("login/", LoginApiView.as_view(), name="login_api"),
    path("profile/", ProfileListApiView.as_view(), name="profile_api"),
]
