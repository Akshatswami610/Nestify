from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Requests
from .serializers import RequestsSerializer

class RequestsViewSet(viewsets.ModelViewSet):
    serializer_class = RequestsSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Requests.objects.all()