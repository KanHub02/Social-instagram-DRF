from ..validators import phone_regex
from rest_framework import serializers
from ..models import User


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
    follows_count = serializers.SerializerMethodField(
        method_name="get_follows_count", read_only=True
    )

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
            "follows_count",
        ]

    def get_followers_count(self, obj):
        if obj:
            return User.objects.filter(user_from=obj).count()

    def get_follows_count(self, obj):
        if obj:
            return User.objects.filter(user_to=obj).count()
