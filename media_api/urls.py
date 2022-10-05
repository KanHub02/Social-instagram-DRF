from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    PostLikesApiView,
    AddLikePostView,
    PostCommentsApiView,
    AddCommentView,
)


router = DefaultRouter()
router.register(r"post", PostViewSet, "post_api")


urlpatterns = [
    path("", include(router.urls), name=""),
    path("post/<pk>/likes/", PostLikesApiView.as_view(), name="get_post_likes"),
    path("post/<pk>/add-like/", AddLikePostView.as_view(), name="add_post_like"),
    path(
        "post/<pk>/comments/", PostCommentsApiView.as_view(), name="get_post_comments"
    ),
    path("post/<pk>/add-comment>/", AddCommentView.as_view(), name="add_post_comment"),
]
