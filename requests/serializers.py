from rest_framework import serializers
from .models import Requests


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ['name', 'phone_number', 'pg_id','date','time']