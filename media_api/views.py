from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post, Like, Comment
from rest_framework import permissions, viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer, CommentSerializer, LikePostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .permissions import IfPostFromUserPermission


# from .pagination import CommentPagination, PostPagination, LikePagination


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IfPostFromUserPermission]
    authentication_classes = [
        JWTAuthentication,
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLikesApiView(APIView):
    serializer_class = LikePostSerializer

    # pagination_classes = LikePagination

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        likes_data = self.serializer_class(
            post.like, many=True, context={"request": request}
        ).data

        return Response(data=likes_data)


class AddLikePostView(generics.CreateAPIView):
    serializer_class = LikePostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = LikePostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(post=post, author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostCommentsApiView(APIView):
    serializer_class = CommentSerializer

    # pagination_classes = CommentPagination

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments_data = self.serializer_class(
            post.comments, many=True, context={"request": request}
        ).data

        return Response(data=comments_data)


class AddCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    authentication_classes = [
        JWTAuthentication,
    ]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(post=post, author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
