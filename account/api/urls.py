from .views import LoginAPIView, registration_view
from django.urls import path


urlpatterns= [
    path('api/login/', LoginAPIView.as_view(), name='login_api'),
    path('api/register/',registration_view,name='api_register'),
]