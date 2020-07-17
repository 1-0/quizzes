from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class UserCard(models.Model):
    """UserCard - class for user card content"""
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=settings.MEDIA_URL, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
