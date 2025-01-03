from django.db import models

from lead.models import Lead


class Note(models.Model):
    lead = models.ForeignKey(Lead, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)