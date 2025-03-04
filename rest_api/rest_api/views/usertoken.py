from ..serializers import RegisterUserTokenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class RegisterUserTokenView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        try:
                serializer = RegisterUserTokenSerializer(data=request.data)
                if serializer.is_valid():
                        # Simpan data ke database
                        serializer.save()
                        # Mengirim respons dengan custom message
                        return Response({
                            'message': 'Users successfully created!',  # Custom message
                            'data': serializer.data,  # Data yang disimpan
                        }, status=status.HTTP_201_CREATED)
                # Jika data tidak valid, kembalikan pesan error
                else : 
                    return Response({
                    'message': 'Validation failed', 
                    'errors':serializer.errors,
                    'status':status.HTTP_400_BAD_REQUEST
                    }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e :
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
    
        
               