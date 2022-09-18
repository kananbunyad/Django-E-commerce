from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
from django.forms import DecimalField
from phonenumber_field.modelfields import PhoneNumberField
USER = get_user_model()






class Order(models.Model):
    user            =  models.ForeignKey(USER, on_delete=models.CASCADE)
    status          =  models.CharField(max_length=255)
    basket          =  models.ForeignKey('Basket', on_delete=models.SET_NULL, null=True) 
    total_price     =  DecimalField(max_digits = 5,decimal_places = 2)
    checkout_adress =  models.ForeignKey('CheckoutMethod', on_delete=models.SET_NULL, blank=True, null=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.status} - {self.basket} - {self.total_price}"


class Basket(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE,related_name='basketofuser') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.created_at} - {self.updated_at}"


class BasketItem(models.Model):
    basket = models.ForeignKey("Basket", on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    product_property_values_ids = models.ForeignKey("product.ProductPropertieValue", on_delete=models.CASCADE, null=True, blank=True) 
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.basket} - {self.price} - {self.product_property_values_ids} - {self.product}"





class Wishlist(models.Model):
    user     =     models.OneToOneField(USER, on_delete=models.CASCADE, null=True, blank=True, related_name="wishlistofUser")
    product  =     models.ManyToManyField(Product, related_name="wishlist_products")

    def __str__(self):
        return f"{self.user}'s Wishlist"


class CheckoutMethod(models.Model):
    user        =  models.OneToOneField(USER, on_delete=models.CASCADE, null=True, blank=True)
    first_name  =  models.CharField(max_length=50)
    last_name   =  models.CharField(max_length=50)
    address     =  models.CharField(max_length=50)
    city        =  models.CharField(max_length=50)
    country     =  models.CharField(max_length=50)
    zipcode     =  models.CharField(max_length=50)
    phone       =  PhoneNumberField(null=False, blank=False,unique=True)

    def __str__(self):
        return self.first_name


class ChecoutBilling(models.Model):
    user        = models.ForeignKey(USER, on_delete=models.CASCADE, null=True, blank=True)

    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    address     = models.CharField(max_length=100)
    city        = models.CharField(max_length=50)
    zipcode     = models.CharField(max_length=50)
    country     = models.CharField(max_length=50)
    phone       = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.address
