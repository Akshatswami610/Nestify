from rest_framework import viewsets, permissions
from .models import Requests
from .serializers import RequestsSerializer


class RequestsViewSet(viewsets.ModelViewSet):
    serializer_class = RequestsSerializer

    def get_permissions(self):
        # Allow anyone to create (POST)
        if self.action == 'create':
            return [permissions.AllowAny()]
        # Require authentication for all other actions
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        # Only show requests belonging to the logged-in user
        user = self.request.user
        return Requests.objects.filter(pg__owner=user)

    def perform_create(self, serializer):
        # Optional: attach user if needed (depends on your model)
        if self.request.user.is_authenticated:
            serializer.save(created_by=self.request.user)
        else:
            serializer.save()