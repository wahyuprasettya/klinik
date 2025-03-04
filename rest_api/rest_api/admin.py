# app/admin.py

from django.contrib import admin
from .models import Doctor,Patient,Appointment,Article
  
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Article)
