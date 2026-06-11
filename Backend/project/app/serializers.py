from rest_framework import serializers
from .models import Contact



class ContactSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'