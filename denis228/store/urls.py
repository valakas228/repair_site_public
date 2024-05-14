from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.store, name='store'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)