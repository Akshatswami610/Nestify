
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import *
from django.conf import settings
import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('', home, name='home'),
    path('home', home, name='home'),
    path('pg', pg, name='pg'),
]



# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)