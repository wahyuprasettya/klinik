from rest_framework import generics
from ..models import Patient
from ..serializers import PatientSerializer
from rest_framework import generics
from ..models import Doctor
from ..serializers import DoctorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import UpdateAPIView

class PatientListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class ListPatientView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            patient = Patient.objects.all()
            serializer = PatientSerializer(patient,many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
#untuk menambahkan data pasien
class AddPatient(APIView):
     def post(self, request, *args, **kwargs):
        try:
            serializer = PatientSerializer(data=request.data)
            if serializer.is_valid():
                    # Simpan data ke database
                    serializer.save()
                    # Mengirim respons dengan custom message
                    return Response({
                        'message': 'Item successfully created!',  # Custom message
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

#untuk mendapatkan data pasien by id
class PatienteDetailView(APIView):
    def get(self, request,pk ):
        try:
            patient = Patient.objects.get(id=pk)
            # Gunakan serializer untuk menstrukturkan data
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response(
                {
                    "errors": "data not found",
                    "status":status.HTTP_404_NOT_FOUND
                 
                },
                status=status.HTTP_404_NOT_FOUND
            )
   
class UpdatePatient(UpdateAPIView):
    
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def patch(self, request, *args, **kwargs):
        patient = self.get_object() 
        serializer = self.get_serializer(patient, data=request.data, partial=True)  # Gunakan partial=True

        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
   
        
class PatientDelete(APIView):
    def delete(self,request ,pk):
        try:
            patient= Patient.objects.get(id=pk)
        except Patient.DoesNotExist:
            return Response({
                'error':'data not found'
            },status=status.HTTP_404_NOT_FOUND)
        #Delete the item from the database 
        patient.delete()

        #Return a 284 response
        return Response({"Success Deleted"},status=status.HTTP_200_OK)
    
        
        
 