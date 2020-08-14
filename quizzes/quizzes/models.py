from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

FS = FileSystemStorage(location=settings.MEDIA_ROOT+'quizzes/')


class Quizzes(models.Model):
    """Quizzes - class for quizzes content"""
    title = models.CharField(max_length=255, unique=True)
    q_person = models.ManyToManyField(User)
    photo = models.ImageField(
        storage=FS,
        null=True,
        blank=True
    )
    content = models.TextField()
    is_publ = models.BooleanField(default=False)
    publ_d_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    readonly_fields = ('published_datetime',)
    ordering = ['-publ_d_time', 'title']


class Question(models.Model):
    """Question - class for quizzes questions"""
    quizzes = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    photo = models.ImageField(
        # upload_to=settings.MEDIA_URL+'questions/%d-%m-%YT%H.%M.%S.%f/',
        storage=FS,
        null=True,
        blank=True
    )
    content = models.TextField()


class Answer(models.Model):
    """Answer - class for quizzes questions answers"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    photo = models.ImageField(
        storage=FS,
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

    readonly_fields = ('published_datetime',)

