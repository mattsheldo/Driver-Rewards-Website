from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login-home'),
    path('create/', views.createAcc, name='createAcc-home'),
    path('logout/', views.logout, name='logout-home'),
    path('home/', views.home, name='home-home'),
]
