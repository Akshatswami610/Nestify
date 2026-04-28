from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PG, PGImage

User = get_user_model()


# ─────────────────────────────
# Owner Serializer (NEW)
# ─────────────────────────────
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone_number',  # ⚠️ make sure this exists in your User model
        ]


# ─────────────────────────────
# PG Image Serializer
# ─────────────────────────────
class PGImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGImage
        fields = ['id', 'image']


# ─────────────────────────────
# PG Serializer (UPDATED)
# ─────────────────────────────
class PGSerializer(serializers.ModelSerializer):
    images = PGImageSerializer(many=True, read_only=True)

    # ✅ FIX: return full owner object instead of just username
    owner = OwnerSerializer(read_only=True)

    # for uploading multiple images
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = PG
        fields = [
            'pg_id',
            'owner',  # now contains full owner data
            'name',
            'description',
            'rent',
            'deposit',
            'booking_fees',
            'location',
            'city',
            'wifi',
            'food',
            'laundry',
            'ac',
            'parking',
            'gender_preference',
            'is_available',
            'created_at',
            'images',           # for GET
            'uploaded_images',  # for POST/PUT
        ]

    # ─────────────────────────────
    # CREATE with images
    # ─────────────────────────────
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])

        # owner should come from request.user in view
        pg = PG.objects.create(**validated_data)

        for image in uploaded_images:
            PGImage.objects.create(pg=pg, image=image)

        return pg

    # ─────────────────────────────
    # UPDATE with optional new images
    # ─────────────────────────────
    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])

        # update PG fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        # add new images (does NOT delete old ones)
        for image in uploaded_images:
            PGImage.objects.create(pg=instance, image=image)

        return instance