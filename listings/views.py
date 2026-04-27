from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import PG
from .serializers import PGSerializer


class PGViewSet(viewsets.ModelViewSet):
    serializer_class = PGSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 🔍 Get all PGs + filtering
    def get_queryset(self):
        user = self.request.user

        # If user is authenticated → only their listings
        if user.is_authenticated:
            queryset = PG.objects.filter(owner=user).order_by('-created_at')
        else:
            # Public users → see all available PGs
            queryset = PG.objects.filter(is_available=True).order_by('-created_at')

        # 🔍 Filters (keep your existing filters)
        city = self.request.query_params.get('city')
        max_rent = self.request.query_params.get('max_rent')
        wifi = self.request.query_params.get('wifi')
        food = self.request.query_params.get('food')
        gender = self.request.query_params.get('gender')

        if city:
            queryset = queryset.filter(city__icontains=city)

        if max_rent:
            queryset = queryset.filter(rent__lte=max_rent)

        if wifi is not None:
            queryset = queryset.filter(wifi=wifi.lower() == 'true')

        if food is not None:
            queryset = queryset.filter(food=food.lower() == 'true')

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