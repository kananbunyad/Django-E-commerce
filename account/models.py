
from django.db import models
# from django.contrib.auth import get_user_model
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import ListView

# User = get_user_model()

# class UserListView(LoginRequiredMixin, ListView):
#     model = User
#     template_name = "user_detail.html"
    

class Subscriber(models.Model):
    email = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class AccountInformation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=55)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.first_name

