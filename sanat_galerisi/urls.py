from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('artworks/', include('artworks.urls')),
    path('events/', include('events.urls')),
    path('reservations/', include('reservations.urls')),
    path('orders/', include('orders.urls')),
    path('reviews/', include('reviews.urls')),
]