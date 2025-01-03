from django.db import models

from lead.models import Lead

class Contact(models.Model):
    lead = models.ForeignKey(Lead, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
