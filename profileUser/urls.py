from django.urls import path

from profileUser import views

app_name = 'profile'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_validation/', views.profile_validation,
         name='profile_validation'),
    path('patient/', views.profile_Patinet,
         name='patinet'),
    path('patient/validation', views.profile_Patinet_validation,
         name='patient_validation'),
    path('doctor/', views.profile_Doctor,
         name='doctor'),
    path('doctor/validation', views.profile_Doctor_validation,
         name='doctor_validation'),
    # path('user/', views.Profile_User,name='user'),

]
