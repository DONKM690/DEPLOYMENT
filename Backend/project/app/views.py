from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerialiser

# Create your views here.

@api_view(['POST'])
def contact_create(request):
    serializer = ContactSerialiser(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "Contact Form Created Successfully"
        })
    return Response(serializer.errors)
