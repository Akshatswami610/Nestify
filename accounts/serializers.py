from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


# -----------------------------
# REGISTER SERIALIZER
# -----------------------------
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone_number']

    def validate_email(self, value):
        if value and User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_phone_number(self, value):
        if value and User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Phone number already exists")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# -----------------------------
# LOGIN SERIALIZER
# -----------------------------
class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()  # email / phone / username
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['identifier'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")

        return user


# -----------------------------
# USER SERIALIZER
# -----------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number']