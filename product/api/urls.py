from django.urls import path
from .views import CategoriesAPI,ProductAPI,CategoriesReadUpdateDeleteViewAPI

urlpatterns = [
    path('api/category/',CategoriesAPI.as_view(),name = 'api_category'),
    path('api/category/<int:pk>/',CategoriesReadUpdateDeleteViewAPI.as_view(),name = 'api_detail_category'),
    path('api/products/',ProductAPI.as_view(),name = 'api_products'),
    path('api/products/<int:pk>/',ProductAPI.as_view(),name = 'api_detail_products'),
]