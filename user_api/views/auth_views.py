from ..serializers.auth_serializers import UserRegisterSerializer, LoginSerializer
from rest_framework import generics
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


from ..permissions import IsAnonymous

from ..models import User


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
