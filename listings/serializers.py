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
            'images',           # for GET
            'uploaded_images',  # for POST/PUT
        ]

    # ✅ CREATE with images
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        pg = PG.objects.create(**validated_data)

        for image in uploaded_images:
            PGImage.objects.create(pg=pg, image=image)

        return pg

    # ✅ UPDATE with optional new images
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