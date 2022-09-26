from django.urls import path, include
from .views import UserRegisterApiView, LoginApiView


urlpatterns = [
    path("register/", UserRegisterApiView.as_view(), name="register_api"),
    path("login/", LoginApiView.as_view(), name="login_api"),
]
