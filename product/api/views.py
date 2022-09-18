from requests import request
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
    )
from product.models import Categories
from django.views.generic.detail import DetailView
from product.models import Product
from .serializers import CategoriesReadSerializer,ProductSerializer,CategoriesCreateSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status



class GenericAPIViewSerializerMixin:


    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]
      



class CategoriesAPI(GenericAPIViewSerializerMixin,ListCreateAPIView,DetailView):
    queryset = Categories.objects.all()
   
    serializer_classes = {
        'GET': CategoriesReadSerializer,
        'POST': CategoriesCreateSerializer,
    }
        


class CategoriesReadUpdateDeleteViewAPI(GenericAPIViewSerializerMixin,RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_classes = {
        'GET': CategoriesReadSerializer,
        'PUT':  CategoriesCreateSerializer,
        'PATCH': CategoriesCreateSerializer,
        'DELETE': CategoriesCreateSerializer,

    } 




class ProductAPI(APIView):

    # def get(self,*args,**kwargs):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products,context={'request':request},many=True)
    #     return JsonResponse(serializer.data,safe=False)            


    def get(self, request, *args, **kwargs):
        arr = []
        for item in Product.objects.all():
            serializer = ProductSerializer(item)
            arr.append(serializer.data)
        return Response(arr, status=status.HTTP_200_OK) 

    def post(self,request,*args,**kwargs):
        form_data = request.data
        serializer = ProductSerializer(data=form_data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data,safe=False)



    def put(self, request, *args,**kwargs):

        serializer = ProductSerializer(data=request.data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors,safe= False)
        else:
            data = serializer.data
            data['id'] = id
            d = data.save()
            serializer = ProductSerializer(d)
            return JsonResponse(serializer.data ,safe= False)



    def patch(self,request,*args,**kwargs):
        id= kwargs['id']
        products = Product.objects.get(id=id)
        products_data = request.data
        serializer = ProductSerializer(data=products_data,partial=True,instance=products)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data,safe=False,status=200)
