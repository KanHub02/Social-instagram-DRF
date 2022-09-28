from email.policy import default
from ..validators import phone_regex
from rest_framework import serializers
from ..models import User, OnlineUserActivity, FollowerSystem
from rest_framework import response
from rest_framework import status


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=35, read_only=True)
    user_avatar = serializers.CharField(max_length=500, required=False)
    bio = serializers.CharField(max_length=255, required=False)
    about_me = serializers.CharField(max_length=255, required=False)
    phone_number = serializers.CharField(
        max_length=12, validators=[phone_regex],
        required=False
    )
    follows_count = serializers.SerializerMethodField(
        method_name="get_follows_count", read_only=True
    )
    followers_count = serializers.SerializerMethodField(
        method_name="get_followers_count", read_only=True
    )
    last_online = serializers.StringRelatedField()

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
            "last_online"
        ]

    def get_follows_count(self, obj):
        return FollowerSystem.objects.filter(user_to=obj).count()
        
    def get_followers_count(self, obj):
        return FollowerSystem.objects.filter(user_from=obj).count()
