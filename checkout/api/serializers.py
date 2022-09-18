from itertools import product
from rest_framework import serializers
from checkout.models import Basket, BasketItem
from product.models import Product
from product.api.serializers import ProductSerializer 


class BasketSerializer(serializers.ModelSerializer):


    class Meta:
        model = Basket
        fields = (
            'id',
            'user',
        )


class BasketItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = BasketItem
        fields = (
            'product',
            'id',
            'product_id',
            'quantity',
            'price',
        )

    def create(self, validated_data):
        product_id = validated_data.pop('product_id')
        basket, created = Basket.objects.get_or_create(user=self.context['request'].user)
        price = Product.objects.get(id=product_id).price
        basket_item, created = BasketItem.objects.get_or_create(basket=basket, product_id=product_id)
        if not created:
            basket_item.quantity += 1
            basket_item.price += price
            basket_item.save()
        else:
            basket_item.quantity = 1
            basket_item.price = price
            basket_item.save()
        return basket_item

    def get(self, request, *args, **kwargs):
        basket, created = Basket.objects.get_or_create(user=self.context['request'].user)
        basket_items = BasketItem.objects.filter(basket=basket)
        return {
            'basket_items': basket_items,
        }

    def delete(self, request, *args, **kwargs):
        basket, created = Basket.objects.get_or_create(user=self.context['request'].user)
        basket_items = BasketItem.objects.filter(basket=basket)
        basket_items.delete()
        return {
            'basket_items': basket_items,
        }