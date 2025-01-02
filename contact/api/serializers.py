from contact.models import Contact
from lead.api.serializers import LeadSerializer
from rest_framework import serializers



class ContactSerializer(serializers.ModelSerializer):
    lead = LeadSerializer() 
    class Meta:
        model = Contact
        fields = ['id', 'lead', 'name', 'email', 'phone']
