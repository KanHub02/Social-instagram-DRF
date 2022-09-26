from rest_framework import serializers
from ..models import User, Followers
from rest_framework import status


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=35)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=40, write_only=True)
    password2 = serializers.CharField(max_length=40, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

    def validate(self, attrs):
        if attrs["password2"] != attrs["password"]:
            raise serializers.ValidationError("Passwords didn't match!")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=35)
    password = serializers.CharField(max_length=40, write_only=True)
