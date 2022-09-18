from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static  
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('',include('account.api.urls')),
    path('',include('product.api.urls')),
    path('',include('checkout.api.urls')),
]


urlpatterns += i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('account.urls')),
    path('', include('checkout.urls')),
    path('', include('core.urls')),
    path('', include('product.urls')),
)
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  