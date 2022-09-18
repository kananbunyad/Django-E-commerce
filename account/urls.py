from django.urls import path,include
from . views import PasswordsChangeView,RegisterView,Activate
from django.contrib.auth import views 
from . import views 




urlpatterns = [
    path('account_info/', views.account_info, name='account_info'),
    path('accounts/login/', views.login_page, name='login'),
    path("logout", views.logout_page, name= "logout_page"),
    path('change_password/', PasswordsChangeView.as_view(template_name='change_password.html')),
    path('change-succes/',views.change_succes, name = "change_succes"),
    path('profile/',views.user_profile, name= "user_profile"),
    path('activate/<str:uidb64>/<str:token>/',Activate.as_view(),name= "activate"),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('social_django.urls', namespace='social')),
] 
