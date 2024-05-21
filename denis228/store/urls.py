from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.store, name='store'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add_comment/<slug:slug>/', views.add_comment, name='add_comment'),
    path('add_to_cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)