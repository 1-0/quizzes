from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Quizzes(models.Model):
    """Quizzes - class for quizzes content"""
    person = models.ManyToManyField(User)
    image = models.ImageField(
        upload_to=settings.MEDIA_URL+'quizzes/%d-%m-%YT%H.%M.%S.%f/',
        null=True,
        blank=True
    )
    content = models.TextField()
    published = models.BooleanField(default=True)
    published_datetime = models.DateTimeField(auto_now=True)


class Question(models.Model):
    """Question - class for quizzes questions"""
    quizzes = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=settings.MEDIA_URL+'questions/%d-%m-%YT%H.%M.%S.%f/',
        null=True,
        blank=True
    )
    content = models.TextField()


class Answer(models.Model):
    """Answer - class for quizzes questions answers"""
    question = models.ManyToManyField(Question, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=settings.MEDIA_URL+'answers/%d-%m-%YT%H.%M.%S.%f/',
        null=True,
        blank=True
    )
    content = models.TextField()
    correct = models.BooleanField()


class Comment(models.Model):
    """Comment - class for quizzes Comments"""
    quizzes = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.TextField()
    published_datetime = models.DateTimeField(auto_now=True)
    allowed = models.BooleanField(default=True)
