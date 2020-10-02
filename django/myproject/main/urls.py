from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('create/', views.createAcc, name='createAcc-home'),
    path('create/', views.createAcc, name='createAcc-home'),
    path('logout/create/', views.createAcc, name='createAcc-home2'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout/logout.html'), name='logout'),
    path('home/', views.home, name='home-home'),
    path('home/logout/', auth_views.LogoutView.as_view(template_name='logout/logout.html'), name='logout2'),
    path('', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
]
