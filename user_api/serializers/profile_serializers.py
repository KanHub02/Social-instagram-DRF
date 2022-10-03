from curses.ascii import US
from email.policy import default
from unittest.util import _MAX_LENGTH
from ..validators import phone_regex
from rest_framework import serializers
from ..models import User, OnlineUserActivity, FollowerSystem
from rest_framework import response
from rest_framework import status


class FollowerSystemSerializer(serializers.ModelSerializer):
    user_from = serializers.CurrentUserDefault
    user_to  = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = FollowerSystem
        fields = ["user_to"]


class GetUserIdSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ["id"]


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineUserActivity
        fields = ["last_activity"]





class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=35)
    user_avatar = serializers.CharField(max_length=500, required=False)
    bio = serializers.CharField(max_length=255, required=False)
    about_me = serializers.CharField(max_length=255, required=False)
    phone_number = serializers.CharField(
        max_length=12, validators=[phone_regex], required=False
    )
    follows_count = serializers.SerializerMethodField(
        method_name="get_follows_count", read_only=True
    )
    followers_count = serializers.SerializerMethodField(
        method_name="get_followers_count", read_only=True
    )
    last_activity = UserActivitySerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "user_avatar",
            "about_me",
            "bio",
            "phone_number",
            "follows_count",
            "followers_count",
            "last_activity",
            "is_private",
        ]

    def get_follows_count(self, obj):
        return FollowerSystem.objects.filter(user_to=obj).count()

    def get_followers_count(self, obj):
        return FollowerSystem.objects.filter(user_from=obj).count()


class PrivateStatusSerializer(serializers.ModelSerializer):
    is_private = serializers.BooleanField(default=serializers.CurrentUserDefault())

    class Meta:
        model = User
        fields = ["id", "is_private"]

    def update(self, instance, validated_data):
        instance.is_private = validated_data.get("is_private", instance.is_private)
        instance.save()
        return instance


class GetAllFollowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowerSystem
        fields = ["user_to"]


class GetAllFollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowerSystem
        fields = ["user_from"]
