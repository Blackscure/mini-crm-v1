from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone', 'created_by', 'created_at']
        read_only_fields = ['id', 'created_at', 'created_by']

    def validate_email(self, value):
        """
        Validate that the email is unique.
        """
        if Lead.objects.filter(email=value).exists():
            raise serializers.ValidationError("A lead with this email already exists.")
        return value
