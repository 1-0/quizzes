from django import forms
from .models import Quizzes, Question, Answer


# class Quizzes(models.Model):
#     """Quizzes - class for quizzes content"""
#     person = models.ManyToManyField(User)
#     image = models.ImageField(
#         upload_to=settings.MEDIA_URL+'quizzes/%d-%m-%YT%H.%M.%S.%f/',
#         null=True,
#         blank=True
#     )
#     content = models.TextField()
#     published = models.BooleanField(default=True)
#     published_datetime = models.DateTimeField(auto_now=True)


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('content', 'image', 'correct')
        labels = {
            'content': 'Answer content',
            'image': 'Answer image',
            'correct': 'Correct answer',
        }
        widgets = {
            'content': forms.Textarea(attrs={'type': 'html'}),
            'correct': forms.BooleanField()
        }


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('content', 'image')
        labels = {
            'content': 'Question content',
            'image': 'Question image',
        }
        widgets = {
            'content': forms.Textarea(attrs={'type': 'html'}),
        }


class QuizzesForm(forms.ModelForm):

    class Meta:
        model = Quizzes
        fields = ('content', 'image', 'published', 'published_datetime')
        labels = {
            'content': 'Quizzes content',
            'image': 'Quizzes image',
            'published': 'Quizzes published',
            'published_datetime': 'Quizzes published datetime',
        }
        widgets = {
            'content': forms.Textarea(attrs={'type': 'html'}),
            'published': forms.BooleanField()
        }
