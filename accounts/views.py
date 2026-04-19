from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model

from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()


# -----------------------------
# REGISTER VIEW
# -----------------------------
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
# LOGIN VIEW
# -----------------------------
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        identifier = request.data.get("email") or request.data.get("phone")
        password = request.data.get("password")

        # Validate input
        if not identifier or not password:
            return Response(
                {"error": "Email/Phone and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Authenticate using custom backend (email OR phone)
        user = authenticate(request, username=identifier, password=password)

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Check if user is active
        if not user.is_active:
            return Response(
                {"error": "Account is disabled"},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Generate or get token
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user": UserSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )