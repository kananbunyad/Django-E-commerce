
from django.contrib import admin
from checkout.models import Order,Basket,BasketItem,CheckoutMethod,ChecoutBilling

admin.site.register([Order,Basket,BasketItem,CheckoutMethod,ChecoutBilling])
# Register your models here.
