from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import PG
from .serializers import PGSerializer


class PGViewSet(viewsets.ModelViewSet):
    serializer_class = PGSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 🔍 Get all PGs + filtering
    def get_queryset(self):
        queryset = PG.objects.all().order_by('-created_at')

        # Filters
        city = self.request.query_params.get('city')
        max_rent = self.request.query_params.get('max_rent')
        wifi = self.request.query_params.get('wifi')
        food = self.request.query_params.get('food')
        gender = self.request.query_params.get('gender')

        if city:
            queryset = queryset.filter(city__icontains=city)

        if max_rent:
            queryset = queryset.filter(rent__lte=max_rent)

        if wifi:
            queryset = queryset.filter(wifi=True)

        if food:
            queryset = queryset.filter(food=True)

        if gender:
            queryset = queryset.filter(gender_preference=gender)

        return queryset

    # 🧑‍💼 Assign owner automatically on create
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # 🔒 Only owner can update/delete
    def perform_update(self, serializer):
        if self.request.user != serializer.instance.owner:
            raise PermissionDenied("You are not allowed to edit this PG")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.owner:
            raise PermissionDenied("You are not allowed to delete this PG")
        instance.delete()