from ..serializers.profile_serializers import (
    ProfileSerializer,
    PrivateStatusSerializer,
    GetAllFollowersSerializer,
    GetAllFollowsSerializer,
    FollowerSystemSerializer,
    UnFollowByCurrentUserSerializer,
)

from rest_framework import generics
from rest_framework import views
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import FollowerSystem, User
from media_api.models import Post

from ..permissions import (
    UserProfilePermission,
    CustomAuthenticatedPermission,
)


class UnFollowByView(generics.DestroyAPIView):

    queryset = FollowerSystem.objects.all()
    serializer_class = UnFollowByCurrentUserSerializer
    permission_classes = [
        UserProfilePermission,
    ]
    authentication_classes = [JWTAuthentication]

    def destroy(self, request, pk):
        user = FollowerSystem.objects.get(user_to_id=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_destroy(user)
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data="Current user unfollow succesfully",
            )


class GetToFollowView(views.APIView):
    serializer_class = FollowerSystemSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        JWTAuthentication,
    ]

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user_from=request.user, user_to=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllFollows(generics.ListAPIView):
    serializer_class = GetAllFollowsSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    # pagination_classes = CommentPagination

    def get(self, request, pk):
        post = get_object_or_404(User, pk=pk)
        follows_data = self.serializer_class(
            post.from_set, many=True, context={"request": request}
        ).data

        return Response(data=follows_data)


class GetAllFollowers(generics.ListAPIView):
    serializer_class = GetAllFollowersSerializer
    [
        IsAuthenticated,
    ]

    def get(self, request, pk):
        post = get_object_or_404(User, pk=pk)
        followers_data = self.serializer_class(
            post.to_set, many=True, context={"request": request}
        ).data

        return Response(data=followers_data)


class ProfileViewSet(ReadOnlyModelViewSet):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, CustomAuthenticatedPermission]
    authentication_classes = [
        JWTAuthentication,
    ]


class ProfileUpdateApiView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [UserProfilePermission]
    authentication_classes = [JWTAuthentication]


class UserSetPrivateStatus(generics.UpdateAPIView):
    permission_classes = [UserProfilePermission]
    queryset = User.objects.all()
    serializer_class = PrivateStatusSerializer
    authentication_classes = [
        JWTAuthentication,
    ]


class ToSavePostView(views.APIView):
    serializer_class = []
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        JWTAuthentication,
    ]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(saved_post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
