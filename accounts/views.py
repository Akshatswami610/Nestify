from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "phone_number": getattr(user, 'phone_number', ''),
            "company_name": getattr(user, 'company_name', ''),
        })

    def patch(self, request):
        user = request.user
        user.username = request.data.get('username', user.username)
        user.phone_number = request.data.get('phone_number', user.phone_number)
        user.company_name = request.data.get('company_name', user.company_name)
        user.save()

        return Response({"success": True})
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
            "identifier": request.data.get("identifier"),
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