from django.db import models
from django.contrib.auth.models import User
from quizzes.models import Image


class UserCard(models.Model):
    """UserCard - class for user card content"""
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = Image()
    birthday = models.DateField()
    about = models.TextField()
