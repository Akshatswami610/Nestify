from rest_framework.routers import DefaultRouter
from .views import PGViewSet, PGImageViewSet

app_name = 'listings'

router = DefaultRouter()
router.register(r'', PGViewSet, basename='pg')
router.register(r'images', PGImageViewSet, basename='pg-images')

urlpatterns = router.urls  