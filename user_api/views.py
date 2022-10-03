from ast import Is
from operator import ge

from requests import delete
from .serializers.auth_serializers import UserRegisterSerializer, LoginSerializer
from .serializers.profile_serializers import (
    ProfileSerializer,
    PrivateStatusSerializer,
    GetAllFollowersSerializer,
    GetAllFollowsSerializer,
    FollowerSystemSerializer
)

from rest_framework import generics
from rest_framework import views
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated

from .models import FollowerSystem, User

from .permissions import (
    UserProfilePermission,
    IsAnonymous,
    CustomAuthenticatedPermission,
)



class UnFollowView(generics.DestroyAPIView):
    serializer_class = FollowerSystem
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.delete(user_from=request.user, user_to=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        


class GetToFollowView(views.APIView):
    serializer_class = FollowerSystemSerializer
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

    # pagination_classes = CommentPagination

    def get(self, request, pk):
        post = get_object_or_404(User, pk=pk)
        follows_data = self.serializer_class(
            post.from_set, many=True, context={"request": request}
        ).data

        return Response(data=follows_data)


class GetAllFollowers(generics.ListAPIView):
    serializer_class = GetAllFollowersSerializer

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


class UserRegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [
        IsAnonymous,
    ]


class LoginAPIView(views.APIView):
    permission_classes = [IsAnonymous]

    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.data["username"]
                password = serializer.data["password"]
                user = authenticate(username=username, password=password)
                if user is None:
                    data = "User not found"
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST, data={"status": data}
                    )

                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user)

                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "user": user.username,
                        "refresh": str(refresh),
                        "access": str(access),
                    }
                )
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserSetPrivateStatus(generics.UpdateAPIView):
    permission_classes = [UserProfilePermission]
    queryset = User.objects.all()
    serializer_class = PrivateStatusSerializer
    authentication_classes = [
        JWTAuthentication,
    ]
