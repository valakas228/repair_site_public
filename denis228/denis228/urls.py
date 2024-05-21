from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('store/', include('store.urls')),
    path('accounts/', include('accounts.urls')),
]

