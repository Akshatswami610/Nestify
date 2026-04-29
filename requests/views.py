from rest_framework import viewsets, permissions
from .models import Requests
from .serializers import RequestsSerializer

class RequestsViewSet(viewsets.ModelViewSet):
    serializer_class = RequestsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Requests.objects.filter(pg__owner=user)