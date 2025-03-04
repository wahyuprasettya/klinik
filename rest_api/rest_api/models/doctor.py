# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  
    specialization = models.CharField(max_length=100) 
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    practice_schedule = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True,null=True)
    images = models.ImageField(upload_to='images/',blank=True,null=True)
    address = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
