from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import login, signup, logout, ownerdashboard, home, pg, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes (DRF with namespace)
    path('api/v1/accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    #path('api/v1/listings/', include('listings.urls')),
    #path('api/v1/bookings/', include('bookings.urls')),
    #path('api/v1/dashboard/', include('dashboard.urls')),

    # Frontend pages
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('owner-dashboard/', ownerdashboard, name='owner-dashboard'),
    path('pg/', pg, name='pg'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

# Serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)