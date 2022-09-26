from ast import BinOp
from curses.ascii import US
from re import S
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from ..models import User, Followers


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=35)
    user_avatar = serializers.CharField(max_length=500)
    bio = serializers.CharField(max_length=255)
    about_me = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=12)
    followers_count = serializers.SerializerMethodField(
        method_name="get_followers_count"
    )
    follows_count = serializers.SerializerMethodField(method_name="get_follows_count")
    get_user_activities = serializers.TimeField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "user_avatar",
            "about_me",
            "phone_number",
            "followers_count",
            "follows_count",
        ]

    def get_follows_count(self, obj):
        return User.objects.filter(follows=obj).count()

    def get_followers_count(self, obj):
        return User.objects.filter(followers=obj).count()
