from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserRegisterApiView, LoginAPIView, ProfileGetListApiView, ProfileGetView



urlpatterns = [
    path("register/", UserRegisterApiView.as_view(), name="register_api"),
    path("login/", LoginAPIView.as_view(), name="login_api"),
    path("profile/", ProfileGetListApiView.as_view(), name="profile_list"),
    path("profile/<int:pk>/", ProfileGetView.as_view(), name="detail_profile"),
]
