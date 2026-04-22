from rest_framework import serializers
from .models import PG, PGImage


class PGImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGImage
        fields = ['id', 'image']


class PGSerializer(serializers.ModelSerializer):
    images = PGImageSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PG
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'rent',
            'deposit',
            'location',
            'city',
            'wifi',
            'food',
            'laundry',
            'ac',
            'parking',
            'gender_preference',
            'is_available',
            'image',
            'images',
            'created_at',
        ]