from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from accounts.views import(
    RegisterView,
    LoginView, )

router = routers.DefaultRouter()
router.register('users', RegisterView)
router.register('login', LoginView)
router.register('logout', LogoutView)


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]