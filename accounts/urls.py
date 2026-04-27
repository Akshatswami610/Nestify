from django.urls import path
from .views import RegisterView, LoginView, LogoutAPIView, MeView

app_name = 'accounts'  # important for namespacing

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='api-login'),
    path('logout/', LogoutAPIView.as_view(), name='api-logout'),
    path('me/', MeView.as_view(), name='me'),
]