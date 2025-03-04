# myapp/models.py
from django.db import models
from .doctor import Doctor
from django.contrib.auth.models import User

class Patient(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)   
    date_of_birth = models.DateField()
    address = models.TextField()  
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True,null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='patients') 

    def __str__(self):
        return self.name
