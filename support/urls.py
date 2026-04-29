from rest_framework.routers import DefaultRouter
from .views import SupportViewSet

app_name = 'support'

router = DefaultRouter()
router.register(r'', SupportViewSet, basename='support')

urlpatterns = router.urls