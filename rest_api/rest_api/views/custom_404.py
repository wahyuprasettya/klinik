from rest_framework.response import Response
from rest_framework import status

def custom_404(request, exception=None):
    return Response({
        "error": "Not Found",
        "message": "The requested resource was not found on this server.",
        "status_code": 404
    })