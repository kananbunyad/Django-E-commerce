from .views import BasketAPIView,BasketItemAPIView
from django.urls import path


urlpatterns= [
    path('api/basket/', BasketAPIView.as_view(),name='basket'),
    path('api/basketitem/', BasketItemAPIView.as_view(),name='basketitem'),
    path('api/basketitem/<int:pk>/', BasketItemAPIView.as_view(),name='basketitem'),

]