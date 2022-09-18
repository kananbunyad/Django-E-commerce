from django import forms
from django.forms import widgets
from checkout.models import CheckoutMethod, ChecoutBilling

class CheckoutForms(forms.ModelForm):

    class Meta:
        model = CheckoutMethod
        fields = [
            'user',
            'first_name',
            'last_name',
            'address',
            'city',
            'zipcode',
            'country',
            'phone',
 ]

        widgets = {
            'user': widgets.Select(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'input-text'}),
            'last_name': widgets.TextInput(attrs={'class': 'input-text'}),
            'address': widgets.TextInput(attrs={'class': 'input-text'}),
            'city': widgets.TextInput(attrs={'class': 'input-text'}),
            'zipcode': widgets.TextInput(attrs={'class': 'input-text'}),
            'country': widgets.TextInput(attrs={'class': 'input-text'}),
            'phone': widgets.TextInput(attrs={'class': 'input-text'}),
        }


class CheckoutBillingForms(forms.ModelForm):

     class Meta:
        model = ChecoutBilling
        fields = [
            'user',
            'first_name',
            'last_name',
            'address',
            'city',
            'zipcode',
            'country',
            'phone',]

        widgets = {
            'user' : widgets.Select(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'input-text'}),
            'last_name': widgets.TextInput(attrs={'class': 'input-text'}),
            'address': widgets.TextInput(attrs={'class': 'input-text'}),
            'city': widgets.TextInput(attrs={'class': 'input-text'}),
            'zipcode': widgets.TextInput(attrs={'class': 'input-text'}),
            'country': widgets.TextInput(attrs={'class': 'input-text'}),
            'phone': widgets.TextInput(attrs={'class': 'input-text'}),
        }