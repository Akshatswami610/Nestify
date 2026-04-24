from rest_framework.routers import DefaultRouter
from .views import PGViewSet

app_name = 'listings'

router = DefaultRouter()
router.register(r'pgs', PGViewSet, basename='pg')

urlpatterns = router.urls  