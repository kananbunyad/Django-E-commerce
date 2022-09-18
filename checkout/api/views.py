
from rest_framework.generics import ( ListCreateAPIView)
from .serializers import BasketSerializer,BasketItemSerializer
from django.views.generic.detail import DetailView
from checkout.models import Basket, BasketItem
from django.contrib.auth import get_user_model

USER = get_user_model()


class GenericAPIViewSerializerMixin:


    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]
      



class BasketAPIView(GenericAPIViewSerializerMixin,ListCreateAPIView,DetailView):
    queryset = Basket.objects.all()
   
    serializer_classes = {
        'GET': BasketSerializer,
        'POST': BasketSerializer,
    }
        



class GenericAPIViewSerializerMixin:


    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]
      



class BasketItemAPIView(GenericAPIViewSerializerMixin,ListCreateAPIView,DetailView):
    queryset = BasketItem.objects.all()
   
    serializer_classes = {
        'GET': BasketItemSerializer,
        'POST': BasketItemSerializer,
        'DELETE': BasketItemSerializer,
    }
        