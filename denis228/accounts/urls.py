# accounts/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('edit_repair_request/<int:request_id>/', views.edit_repair_request, name='edit_repair_request'),
    path('delete_repair_request/<int:request_id>/', views.delete_repair_request, name='delete_repair_request'),
]
