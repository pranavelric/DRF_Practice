from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'country_code', 'first_name', 'last_name', 'phone_number', 'contact_pic',
                  'is_favourite']
