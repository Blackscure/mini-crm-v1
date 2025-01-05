from lead.models import Lead
from rest_framework import serializers

class LeadSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone', 'created_by', 'created_at']
        read_only_fields = ['id', 'created_at', 'created_by']
