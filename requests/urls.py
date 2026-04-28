from rest_framework.routers import DefaultRouter
from .views import RequestsViewSet

app_name = 'requests'

router = DefaultRouter()
router.register(r'', RequestsViewSet, basename='requests')

urlpatterns = router.urls