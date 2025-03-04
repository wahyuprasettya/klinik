from rest_framework import generics
from ..models import Article
from ..serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class ListArticleView(APIView):
    def get(self,request):
        try:
            article = Article.objects.all()
            serializer = ArticleSerializer(article,many = True)
            # for article in serializer.data:
            #     if doctor['images']:
            #         doctor['images'] = request.build_absolute_uri(doctor['images'])
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
#untuk mendapatkan data dokter by id
class ArticleDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request,pk ):
        try:
            article = Article.objects.get(id=pk)
            # Gunakan serializer untuk menstrukturkan data
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            return Response(
                {
                    "errors": "data not found",
                    "status":status.HTTP_404_NOT_FOUND
                 
                },
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

        

        


    
            
                
     
 
     
