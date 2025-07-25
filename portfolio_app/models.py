from django.db import models

# Create your models here.
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=200)
    subject = models.TextField(blank=True, null=True)
    message = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name or "Anonymous"
