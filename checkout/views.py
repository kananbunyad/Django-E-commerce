from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from checkout.models import BasketItem 
from core.forms import SubscriberForm
from checkout.models import CheckoutMethod, Wishlist
from django.views.generic.list import ListView
from checkout.forms import CheckoutForms,CheckoutBillingForms
from checkout.models import Basket,Order
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View



class CheckoutBillling(View):
    template_name = 'checkout_billing_info.html'
    http_method_names = ['get', 'post']


    def get(self, request):
        form = CheckoutBillingForms()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = CheckoutBillingForms(request.POST)
        if form.is_valid():
            form.save()
            order = Order.objects.create(
                user=request.user,
                basket = Basket.objects.get(user=request.user),
                checkout_adress = CheckoutMethod.objects.get(user=request.user),
                ordered = False
            )
            order.save()
            return redirect(reverse_lazy('shoping_cart'))
        else:
            return render(request, 'checkout_billing_info.html', {'form': form})



def checkout(request):
    form = CheckoutForms()

    if request.method == 'POST':
        form = CheckoutForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('checkout_billing_info'))
    context = {
        'form' : form,
        }
    return render(request, 'checkout.html',context)





def shopping_cart(request):
    form = SubscriberForm()
    basketitems = BasketItem.objects.all()
    totalprice = 0
    for item in basketitems:
        totalprice += item.product.price * item.quantity
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form,
        'basketitems' : basketitems,
        'totalprice' : totalprice
    }
    return render(request, 'shopping_cart.html',context)

def wishlist(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form
    }
    return render(request, 'wishlist.html',context)



class WishlistView(ListView):
    model = Wishlist
    template_name = 'wishlist.html'
    quesyset =  Wishlist.objects.all()
    context_object_name = 'wishlist'
