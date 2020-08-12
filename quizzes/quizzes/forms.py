from django import forms
from .models import Quizzes, Question, Answer


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('content', 'photo', 'correct')
        labels = {
            'content': 'Answer content',
            'photo': 'Answer image',
            'correct': 'Correct answer',
        }
        widgets = {
            'content': forms.Textarea(attrs={'type': 'html'}),
            'correct': forms.BooleanField()
        }


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('content', 'photo')
        labels = {
            'content': 'Question content',
            'photo': 'Question image',
        }
        widgets = {
            'content': forms.Textarea(attrs={'type': 'html'}),
        }


class QuizzesForm(forms.ModelForm):

    ordering = ['-published_datetime',]
    published = forms.BooleanField(show_hidden_initial=True, required=False)
    readonly_fields = ('published_datetime',)

    class Meta:
        model = Quizzes
        fields = ('title', 'content', 'photo', 'published')
        # fields = ('title', 'content', 'image', 'published', 'published_datetime')
        labels = {
            'title': 'Quizzes title',
            'content': 'Quizzes content',
            'photo': 'Quizzes image',
            'published': 'Quizzes published',
            # 'published_datetime': 'Quizzes published datetime',
        }
        widgets = {
            'content': forms.Textarea(attrs={'type': 'html'}),
        }
