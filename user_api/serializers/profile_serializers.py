from ..validators import phone_regex
from rest_framework import serializers
from ..models import User, Followers, OnlineUserActivity


class LastActivitySerializer(serializers.ModelSerializer):
    last_activity = serializers.TimeField()

    class Meta:
        model = OnlineUserActivity
        fields = "__all__"

    def to_representation(self, instance):
        super().to_representation(instance)
        data = OnlineUserActivity.objects.all()
        data["last_activity"]
        return data


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=35, read_only=True)
    user_avatar = serializers.CharField(max_length=500, read_only=True)
    bio = serializers.CharField(max_length=255, read_only=True)
    about_me = serializers.CharField(max_length=255, read_only=True)
    phone_number = serializers.CharField(
        max_length=12, read_only=True, validators=[phone_regex]
    )
    followers_count = serializers.SerializerMethodField(
        method_name="get_followers_count", read_only=True
    )
    last_activity = LastActivitySerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "user_avatar",
            "about_me",
            "bio",
            "phone_number",
            "followers_count",
            "last_activity",
        ]

    def get_followers_count(self, obj):
        if obj:
            return User.objects.filter(followers=obj).count()
