from rest_framework import generics
from ..models import Doctor
from ..serializers import DoctorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.generics import UpdateAPIView


# untuk membuat CRUD yang disediakan DRF
class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# ini digunakan ketika di tarik pakai postman
class ListDoctorView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            doctor = Doctor.objects.all()
            serializer = DoctorSerializer(doctor,many = True)
            for doctor in serializer.data:
                if doctor['images']:
                    doctor['images'] = request.build_absolute_uri(doctor['images'])
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
#untuk mendapatkan data dokter by id
class DoctorDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,pk ):
        try:
            doctor = Doctor.objects.get(id=pk)
            # Gunakan serializer untuk menstrukturkan data
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Doctor.DoesNotExist:
            return Response(
                {
                    "errors": "data not found",
                    "status":status.HTTP_404_NOT_FOUND
                 
                },
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
#untuk menambahkan data dokter
class AddDoctor(APIView):
    #  permission_classes = [IsAuthenticated]
     def post(self, request, *args, **kwargs):
        try:
            serializer = DoctorSerializer(data=request.data)
            if serializer.is_valid():
                # Simpan data ke database
                serializer.save()
                # Mengirim respons dengan custom message
                return Response({
                    'message': 'Item successfully created!',  # Custom message
                    'data': serializer.data,  # Data yang disimpan
                }, status=status.HTTP_201_CREATED)
            
            # Jika data tidak valid, kembalikan pesan error
            else:    
                return Response({
                        'message': 'Validation failed', 
                        'errors':serializer.errors,
                        'status':status.HTTP_400_BAD_REQUEST
                        }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UpdateDoctor(UpdateAPIView):
    
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def patch(self, request, *args, **kwargs):
        doctor = self.get_object() 
        serializer = self.get_serializer(doctor, data=request.data, partial=True)  # Gunakan partial=True

        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteDoctor(APIView):
    def delete(self, request, doctor_id):
        try:
          #Retrieve Iten by ID
          doctor = Doctor.objects.get(id=doctor_id)

        except Doctor.DoesNotExist:
                return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        #Delete the item from the database 
        doctor.delete()

        #Return a 284 response
        return Response({
                    'message': 'Successfully Deleted',  # Custom message
                    'status':status.HTTP_200_OK ,  # Data yang disimpan
                }, status=status.HTTP_201_CREATED)
 

    
            
                
     
 
     
