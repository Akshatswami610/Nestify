from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


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
        serializer = LoginSerializer(data={
            "identifier": request.data.get("email")
                          or request.data.get("phone_number")
                          or request.data.get("username"),
            "password": request.data.get("password")
        })

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user": UserSerializer(user).data,
            "message": "Login successful"
        }, status=status.HTTP_200_OK)


# -----------------------------
# LOGOUT VIEW (API)
# -----------------------------
class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully"})