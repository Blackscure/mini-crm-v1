from lead.models import Lead
from notes.models import Note
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    lead = serializers.PrimaryKeyRelatedField(queryset=Lead.objects.all())
    lead_name = serializers.CharField(source='lead.name', read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'lead', 'lead_name', 'content', 'created_at']
