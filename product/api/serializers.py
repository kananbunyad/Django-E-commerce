from rest_framework import serializers
from product.models import Categories,Product



class CategoriesReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = (
            'id',
            'title',
            'products',
        )


class CategoriesCreateSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Categories
        fields = (
            'id',
            'title',
            'products',
        )
    def get_products(self,obj):
        print('salam')
        serializer = ProductSerializer(obj.products.all(), context=self.context, many = True)
        return serializer.data


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'field_name',
            'price',
            'brand',
            'category',
            'discount',
        )


    # def get_file_abs_url(self, obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_url(obj.field_name.url)


