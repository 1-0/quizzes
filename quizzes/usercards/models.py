from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from quizzes.models import Quizzes
from django.core.files.storage import FileSystemStorage

FS = FileSystemStorage(location=settings.MEDIA_ROOT+'users/')


class UserCard(models.Model):
    """UserCard - class for user card content"""
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        storage=FS,
        null=True,
        blank=True
    )
    birthday = models.DateField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)


class QuizzesProgress(models.Model):
    """QuizzesProgress - class for user progress in quizzes"""
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    quizzes = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    passed_datetime = models.DateTimeField(auto_now=True)
    correct_answers = models.FloatField()
    passed = models.BooleanField()
