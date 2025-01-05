from reminders.models import Reminder
from rest_framework import serializers
from datetime import datetime

class ReminderSerializer(serializers.ModelSerializer):
    scheduled_time = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")  # Enforcing ISO 8601 format

    class Meta:
        model = Reminder
        fields = ['id', 'lead', 'message', 'scheduled_time', 'is_sent', 'created_at']
        read_only_fields = ['id', 'is_sent', 'created_at']

    def validate_scheduled_time(self, value):
        # Ensure that scheduled_time is a valid datetime
        try:
            datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            raise serializers.ValidationError("Invalid datetime format. Use ISO 8601.")
        return value
