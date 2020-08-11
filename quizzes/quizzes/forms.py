from django import forms
from .models import Quizzes, Question, Answer


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

    published = forms.BooleanField(show_hidden_initial=True, required=False)

    class Meta:
        model = Quizzes
        fields = ('title', 'content', 'image', 'published')
        # fields = ('title', 'content', 'image', 'published', 'published_datetime')
        labels = {
            'title': 'Quizzes title',
            'content': 'Quizzes content',
            'image': 'Quizzes image',
            'published': 'Quizzes published',
            # 'published_datetime': 'Quizzes published datetime',
        }
        widgets = {
            'content': forms.Textarea(attrs={'type': 'html'}),
        }
