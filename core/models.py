
from django.db import models



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=55)
    company = models.CharField(max_length=20)
    adress = models.CharField(max_length=55)
    adress_2 = models.CharField(max_length=4)
    telephone = models.CharField(max_length=55)
    comment = models.TextField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.first_name


