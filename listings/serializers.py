from rest_framework import serializers
from .models import PG, PGImage


class PGImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGImage
        fields = ['id', 'image']


class PGSerializer(serializers.ModelSerializer):
    images = PGImageSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    # for uploading multiple images
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = PG
        fields = [
            'id',
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
            'images',           # for GET
            'uploaded_images',  # for POST
        ]