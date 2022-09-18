
from django import forms
from core.models import Contact
from account.models import Subscriber

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'email',
            'company',
            'adress',
            'adress_2',
            'telephone',
            'comment',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Your name',
            'autofocus' : True
            }),

            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email',
            }),


            'company' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Company',
            }), 

            'adress' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Adress',
            }), 

            'adress_2' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Post Code',
            }), 
            'telephone' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Telephone',
            }), 

            'comment' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Comment',
                'rows' : 7,
            }), 
        }



class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder':'SUBSCRIBE',
            })
        }



