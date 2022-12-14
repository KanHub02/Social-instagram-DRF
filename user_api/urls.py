from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views.auth_views import (
    UserRegisterApiView,
    LoginAPIView,
)

from .views.profile_views import (
    ProfileViewSet,
    ProfileUpdateApiView,
    UserSetPrivateStatus,
    GetAllFollows,
    GetAllFollowers,
    GetToFollowView,
    UnFollowByView,
    ToSavePostView,
)


ROUTER = DefaultRouter()
ROUTER.register(r"profile", ProfileViewSet, "profile")


urlpatterns = [
    path("register/", UserRegisterApiView.as_view(), name="register_api"),
    path("login/", LoginAPIView.as_view(), name="login_api"),
    path("", include(ROUTER.urls)),
    path(
        "profile-update/<int:pk>/",
        ProfileUpdateApiView.as_view(),
        name="profile_update",
    ),
    path(
        "profile-set-private/<int:pk>",
        UserSetPrivateStatus.as_view(),
        name="set_private_status_api",
    ),
    path(
        "profile/<pk>/followers/",
        GetAllFollowers.as_view(),
        name="user_all_followers_api",
    ),
    path("profile/<pk>/follows/", GetAllFollows.as_view(), name="user_all_follows_api"),
    path("profile/follow-to/<pk>/", GetToFollowView.as_view(), name="user_follow_api"),
    path(
        "profile/unfollow-from/<pk>/",
        UnFollowByView.as_view(),
    ),
    path("post/<pk>/save/", ToSavePostView.as_view(), name="save_post_api"),
]
