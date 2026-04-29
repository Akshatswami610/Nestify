from rest_framework import serializers
from .models import Requests
from listings.models import PG

class RequestsSerializer(serializers.ModelSerializer):
    pg = serializers.PrimaryKeyRelatedField(queryset=PG.objects.all())
    pg_name = serializers.CharField(source='pg.name', read_only=True)

    class Meta:
        model = Requests
        fields = [
            'id',
            'pg',
            'pg_name',
            'name',
            'phone_number',
            'visit_date',
            'visit_time',
            'status',
            'timestamp',
        ]