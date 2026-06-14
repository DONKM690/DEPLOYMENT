from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerialiser


# CREATE
@api_view(['POST'])
def contact_create(request):
    serializer = ContactSerialiser(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Contact Form Created Successfully"})

    return Response(serializer.errors, status=400)


# READ ALL
@api_view(['GET'])
def contact_list(request):
    contacts = Contact.objects.all().order_by('-id')
    serializer = ContactSerialiser(contacts, many=True)
    return Response(serializer.data)


# READ ONE
@api_view(['GET'])
def contact_detail(request, pk):
    try:
        contact = Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        return Response({"error": "Contact not found"}, status=404)

    serializer = ContactSerialiser(contact)
    return Response(serializer.data)


# UPDATE
@api_view(['PUT'])
def contact_update(request, pk):
    try:
        contact = Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        return Response({"error": "Contact not found"}, status=404)

    serializer = ContactSerialiser(contact, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Contact Updated Successfully"})

    return Response(serializer.errors, status=400)


# DELETE
@api_view(['DELETE'])
def contact_delete(request, pk):
    try:
        contact = Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        return Response({"error": "Contact not found"}, status=404)

    contact.delete()
    return Response({"message": "Contact Deleted Successfully"})