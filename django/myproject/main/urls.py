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
    path('home/drivers/', views.viewMyDrivers, name="driverlist-driverlist"),
    path('home/all_drivers/', views.viewAllDrivers, name="all-drivers-list"),
    path('home/all_sponsors/', views.viewAllSponsors, name="all-sponsors-list"),
    path('home/all_admins/', views.viewAllAdmins, name="all-admins-list"),
    path('home/point_value/', views.UpdatePointVal, name="pointValue"),
    path('home/profile/', views.viewMyProfile, name="profile-profile"),
    path('home/profile/update/', views.updateMyProfile, name="update-profile"),
    path('home/drivers/viewProfile/', views.viewDriverProfile, name="view-driver"),
    path('home/all_drivers/viewProfile/', views.adviewDriverProfile, name="ad-view-driver"),
    path('home/all_sponsors/viewProfile/', views.adviewSponsorProfile, name="ad-view-sponsor"),
    path('home/all_admins/viewProfile/', views.adviewAdminProfile, name="ad-view-admin"),
    path('', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
]
