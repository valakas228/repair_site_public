from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import estimate_cost, get_issues

urlpatterns = [
    path('', views.store, name='store'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add_comment/<slug:slug>/', views.add_comment, name='add_comment'),
    path('add_to_cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('price-list/', views.price_list, name='price_list'),
    path('estimate/', estimate_cost, name='estimate_cost'),
    path('get_issues/', views.get_issues, name='get_issues'),
    path('create_order/<slug:product_slug>/', views.create_order, name='create_order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


