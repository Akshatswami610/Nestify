from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PG, PGImage

User = get_user_model()


# ─────────────────────────────
# Owner Serializer
# ─────────────────────────────
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone_number',
        ]


# ─────────────────────────────
# PG Image Serializer
# ─────────────────────────────
class PGImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGImage
        fields = ['id', 'image']


# ─────────────────────────────
# PG Serializer
# ─────────────────────────────
class PGSerializer(serializers.ModelSerializer):
    images = PGImageSerializer(many=True, read_only=True)
    owner = OwnerSerializer(read_only=True)

    # multiple image upload
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = PG
        fields = [
            'pg_id',
            'owner',
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
            'images',
            'uploaded_images',
        ]

    # ─────────────────────────────
    # VALIDATION (MAX 5 IMAGES TOTAL)
    # ─────────────────────────────
    def validate_uploaded_images(self, value):
        max_images = 5

        # If updating existing PG
        if self.instance:
            existing_count = self.instance.images.count()
        else:
            existing_count = 0

        if existing_count + len(value) > max_images:
            raise serializers.ValidationError(
                f"Maximum {max_images} images allowed. "
                f"You already have {existing_count} images."
            )

        return value

    # ─────────────────────────────
    # CREATE
    # ─────────────────────────────
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])

        pg = PG.objects.create(**validated_data)

        for image in uploaded_images:
            PGImage.objects.create(pg=pg, image=image)

        return pg

    # ─────────────────────────────
    # UPDATE
    # ─────────────────────────────
    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])

        # update fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        # add new images (without deleting old ones)
        for image in uploaded_images:
            PGImage.objects.create(pg=instance, image=image)

        return instance