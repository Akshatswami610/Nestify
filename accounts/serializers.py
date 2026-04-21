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
        fields = ['company_name', 'email', 'phone_number', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Phone number already exists")
        return value

    def create(self, validated_data):
        email = validated_data['email']

        user = User.objects.create_user(
            username=email,  # ✅ use email as username internally
            email=email,
            phone_number=validated_data['phone_number'],
            company_name=validated_data['company_name'],
            password=validated_data['password']
        )
        return user


# -----------------------------
# LOGIN SERIALIZER
# -----------------------------
class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()  # email / phone / username
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['identifier'],  # email
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        return user


# -----------------------------
# USER SERIALIZER
# -----------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number']