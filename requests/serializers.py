from rest_framework import serializers
from .models import Requests

class RequestsSerializer(serializers.ModelSerializer):
    pg_id = serializers.IntegerField(source='pg.id', read_only=True)
    pg_name = serializers.CharField(source='pg.name', read_only=True)

    class Meta:
        model = Requests
        fields = [
            'id',
            'name',
            'phone_number',
            'pg_id',
            'pg_name',
            'visit_date',
            'visit_time',
            'status',
            'timestamp',
        ]