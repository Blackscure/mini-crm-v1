from contact.models import Contact
from lead.api.serializers import LeadSerializer
from lead.models import Lead
from rest_framework import serializers



class ContactSerializer(serializers.ModelSerializer):
    lead = serializers.PrimaryKeyRelatedField(queryset=Lead.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['lead'] = {
            'id': instance.lead.id,
            'name': instance.lead.name
        }
        return data

    class Meta:
        model = Contact
        fields = ['id', 'lead', 'name', 'email', 'phone']
