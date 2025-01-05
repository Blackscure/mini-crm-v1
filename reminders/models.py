from django.db import models

from lead.models import Lead

class Reminder(models.Model):
    lead = models.ForeignKey(Lead, related_name='reminders', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
