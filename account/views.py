from ast import If
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from core.forms import SubscriberForm
# from account.forms import RegisterForm
from account.forms import  LoginForm,PasswordChangingForm,RegisterForm
from django.contrib import messages
from account.forms import AccountInformation
from django.contrib.auth import authenticate, login as django_login,logout as django_logout,get_user_model
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import CreateView
from django.views.generic import CreateView, View
from django.utils.http import urlsafe_base64_decode
from account.tokens import account_activation_token
from django.utils.encoding import force_str
from account.tasks import send_email_confirmation
from django.contrib.sites.shortcuts import get_current_site
from checkout.models import Basket

User = get_user_model()

# from django.views import generic


    
def account_info(request):
    form = AccountInformation()
    form1 = SubscriberForm()
    print(request.POST)
    if request.method == 'POST':
        form = AccountInformation(data=request.POST)
        form1 = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
        elif form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))

    context = {
        'form' : form,
        'form1' : form1
    }
    return render(request,'account_information.html',context)




class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('change_succes')

def change_succes(request):
    return render(request,'change-succes.html')


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = "register.html"    

    def form_valid(self, form):
        result = super().form_valid(form)
        Basket.objects.create(user=self.object)
        send_email_confirmation(user=self.object,current_site = get_current_site(self.request))
        return result


class Activate(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Mail hesabiniz tesdiq olundu')
            return redirect(reverse_lazy('login'))
        else:
            messages.add_message(request, messages.SUCCESS, 'Mail hesabiniz tesdiq olunmadi')
            return redirect(reverse_lazy('home'))

def active(request):
    return render(request,'activation.html')

# def change_password(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PasswordChangeForm(user=request.user,data=request.POST)
#             if form.is_valid():
#                 form.save()
#                 update_session_auth_hash(request,form.user)
#                 messages.success(request,'Sifreniz ugurla yenilendi!!')
#                 return redirect(reverse_lazy('profile/'))
#         else:
#             form = PasswordChangeForm(user=request.user)
#         context = {
#             'form' : form
#         }
#         return render(request, 'change_password.html',context)
#     else:
#         return HttpResponseRedirect('/login/')


def user_profile(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form
    }
    return render(request, 'user-profile.html',context)










# def register_page(request):
#     form = RegisterForm()
#     form2 = SubscriberForm()
#     print(request.POST)
#     if request.method == 'POST':
#         form = RegisterForm(data=request.POST)
#         form2 = SubscriberForm(data = request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.password=make_password(form.cleaned_data['password'])
#             messages.success(request,f'Qeyditatiniz qeyide alindi for !')
#             user.save()
#             return redirect('user_profile')
#         elif form2.is_valid():
#             form2.save()
#             return redirect('home')
#     context = {
#         'form': form,
#         'form2' : form2
#     }
#     return render(request, 'register.html', context)



def login_page(request):
    form = LoginForm() 
    print(request.POST)
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:  
                django_login(request, user)
                messages.add_message(request, messages.SUCCESS, f'Ugurla login oldunuz {user}!')
                return redirect('user_profile')
            else:
                messages.add_message(request, messages.ERROR, 'Adiniz ve ya sifreniz yanlisdir!')
        
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_page(request):
    django_logout(request)    
    messages.add_message(request, messages.SUCCESS, 'Hesabdan cixis etdiniz!')
    return redirect(reverse_lazy('login'))