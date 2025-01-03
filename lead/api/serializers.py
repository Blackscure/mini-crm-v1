from lead.models import Lead
from rest_framework import serializers


class LeadSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone', 'created_by', 'created_at']
        read_only_fields = ['id', 'created_at', 'created_by']


    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError('Name is required.')
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError('Email is required.')
        if '@' not in value:
            raise serializers.ValidationError('Enter a valid email address.')
        return value

    def validate_phone(self, value):
        if not value:
            raise serializers.ValidationError('Phone number is required.')
        if len(value) < 10:
            raise serializers.ValidationError('Phone number must be at least 10 characters long.')
        return value

    def validate_email(self, value):
        """
        Validate that the email is unique.
        """
        if Lead.objects.filter(email=value).exists():
            raise serializers.ValidationError("A lead with this email already exists.")
        return value
