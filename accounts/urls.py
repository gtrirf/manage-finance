from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register_user, name='register')
]
