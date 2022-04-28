#Spotify URL Configuration

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppSpotify/', include('AppSpotify.urls'))
]
