from django import forms
from product.models import ProductReview,Blog_Comment



class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = (
            'value_rate',
            'quality_rate',
            'price_rate',
            'nickname',
            'summary',
            'review'
        )
        widgets = {

            'value_rate' : forms.RadioSelect(attrs={
                'class' : 'radio'
            }),
            'quality_rate' : forms.RadioSelect(attrs={
                'class' : 'radio'
            }),
            'price_rate' : forms.RadioSelect(attrs={
                'class' : 'radio'
            }),
            'nickname':forms.TextInput(attrs={
            'class':'input-text'
            }),
            'summary':forms.TextInput(attrs={
            'class':'input-text'
            }),
            'review': forms.Textarea(attrs={
                'class': 'input-text',
            }),
        }

class BlogForm(forms.ModelForm):
      class Meta:
        model = Blog_Comment
        fields = (
            'name',
            'email',
            'comment',
        )
        widgets = {
            'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Name',
            'cols' : 2,
            }),

            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'E-mail',
                'cols' : 2,
            }),


            'comment' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Comment',
                'rows' : 7,
                'cols' : 7,
            }), 

        }