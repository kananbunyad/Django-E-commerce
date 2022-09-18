from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<slug>/', views.BlogDetailView.as_view(), name='blog'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('quick_view/', views.quick_view, name='quick_view'),

 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)