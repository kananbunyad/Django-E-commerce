
from django import forms
from account.models import AccountInformation
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm


# from account.views import PasswordsChangeView


USER = get_user_model()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Your name',
        'autofocus' : True,
    }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Last name',
    }))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Email',
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password',
        
    }))
    password2 = forms.CharField(label='Confirm Passowrd', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Confirm Password',
    }))
    username = UsernameField(label='UserName', widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username',
    }))
    class Meta:
        model = USER
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'username',
        )

    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user
       


class LoginForm(AuthenticationForm):


    username = UsernameField(label='UserName', widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username',
    }))

    # email = forms.CharField(label='Email', widget=forms.TextInput(attrs={
    #     'class' : 'form-control',
    #     'placeholder' : 'Email',
    #     'id' : 'emailid',
    # }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password',
        
    }))

    class Meta:
        model = USER
        fields = (
            'username',
            # 'email',
            'password',
        )

class AccountInformation(forms.ModelForm):
    class Meta:
        model = AccountInformation
        fields = (
            'first_name',
            'last_name',
            'email',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Your name',
            'autofocus' : True
            }),

            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Last Name',
            }), 

            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email',
            }),

        }





class PasswordChangingForm(PasswordChangeForm):


    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'type' : 'password',
        'placehorder' : 'Old Password',
    }))

    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'type' : 'password',
        'placehorder' : 'New Password',
    }))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'type' : 'password',
        'placehorder' : 'Confirm New Password',
        
    }))

    class Meta:
        model = USER
        fields = (
            'old_password',
            'new_password1',
            'new_password2',
        )