from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

FS = FileSystemStorage(location=settings.MEDIA_ROOT+'quizzes/')


class Quizzes(models.Model):
    """Quizzes - class for quizzes content"""
    title = models.CharField(max_length=255, unique=True)
    q_person = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
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

    def __repr__(self):
        return "<Quizzes #%s from user #%s>" % (self.id, self.q_person_id)

    def __str__(self):
        return "<Quizzes #%s from user #%s>" % (self.id, self.q_person_id)


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

    def __repr__(self):
        return "<Question #%s for quizzes #%s>" % (self.id, self.quizzes_id)

    def __str__(self):
        return "<Question #%s for quizzes #%s>" % (self.id, self.quizzes_id)


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

    def __repr__(self):
        return "<Answer #%s for question #%s>" % (self.id, self.question_id)

    def __str__(self):
        return "<Answer #%s for question #%s>" % (self.id, self.question_id)


class Comment(models.Model):
    """Comment - class for quizzes Comments"""
    quizzes = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.TextField()
    published_datetime = models.DateTimeField(auto_now=True)
    allowed = models.BooleanField(default=True)

    readonly_fields = ('published_datetime',)

    def __repr__(self):
        return "<Comment #%s from user #%s to quizzes #%s>" % (
            self.id,
            self.person_id,
            self.quizzes_id
        )

    def __str__(self):
        return "<Comment #%s from user #%s to quizzes #%s>" % (
            self.id,
            self.person_id,
            self.quizzes_id
        )
