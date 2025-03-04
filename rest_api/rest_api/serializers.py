from rest_framework import serializers
from .models import Doctor
from .models import Patient
from .models import Article
from django.conf import settings
# from .models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
            
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'  # Atau daftar kolom yang ingin disertakan, seperti ['id', 'name', 'description']

# class AppointmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Appointment
#         fields = '__all__'  # Atau daftar kolom yang ingin disertakan, seperti ['id', 'name', 'description']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        
class RegisterUserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username','password','email', 'first_name', 'last_name']
         
    def validate_password(self, value):
        # Hash password sebelum menyimpannya
        return make_password(value)
    
    def create(self, validated_data):
        # Membuat UserProfile baru dengan password yang sudah di-hash
        return User.objects.create(**validated_data)
    
    def to_representation(self, instance):
        # Mengembalikan token JWT setelah registrasi berhasil
        refresh = RefreshToken.for_user(instance)
        return {
            'username': instance.username,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
class LoginUserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        