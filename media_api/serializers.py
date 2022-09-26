from rest_framework import serializers
from .models import Post, Comment, Like
from user_api.models import User


class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    text = serializers.CharField(max_length=255)

    class Meta:
        model = Comment
        fields = ["author", "text"]
        extra_kwargs = {"author": {"read_only": True}}

    def get_count_of_likes(self, obj):
        return Comment.objects.filter(comment=obj).count()


class LikePostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ["author"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(default=serializers.CurrentUserDefault())
    image = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    count_of_comments = serializers.SerializerMethodField(
        method_name="get_count_of_comments"
    )
    likes = serializers.SerializerMethodField(method_name="get_count_of_likes")

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "image",
            "description",
            "likes",
            "count_of_comments",
        ]

    def get_count_of_comments(self, obj):
        return Comment.objects.filter(post=obj).count()

    def get_count_of_likes(self, obj):
        return Like.objects.filter(post=obj).count()
