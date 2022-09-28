from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserRegisterApiView, LoginAPIView, ProfileViewSet

ROUTER = DefaultRouter()
ROUTER.register(r"profile", ProfileViewSet, "profile")


urlpatterns = [
    path("register/", UserRegisterApiView.as_view(), name="register_api"),
    path("login/", LoginAPIView.as_view(), name="login_api"),
    path("", include(ROUTER.urls)),
]
