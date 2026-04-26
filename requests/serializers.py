from rest_framework import serializers
from .models import Requests


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ['name', 'phone_number', 'pg_id','visit_date','visit_time','status']