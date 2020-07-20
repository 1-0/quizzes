from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class UserCard(models.Model):
    """UserCard - class for user card content"""
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=settings.MEDIA_URL, null=True, blank=True)
    birthday = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
