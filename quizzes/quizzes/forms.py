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
    # q_person = forms.UUIDField(
    #     required=False,
    #     label='Person',
    #     widget=forms.HiddenInput(attrs={'hidden': 'true'}),
    #     initial=False,
    # )
    is_publ = forms.BooleanField(
        required=False,
        label='Published',
        widget=forms.CheckboxInput(attrs={'class': 'filled-in'}),
        initial=False,
    )
    ordering = ['-publ_d_time', 'title']
    readonly_fields = ('q_person', 'person', 'publ_d_time')

    class Meta:
        model = Quizzes
        fields = (
            'title',
            'content',
            'photo',
            'is_publ',
            # 'q_person',
        )
        labels = {
            'title': 'Quizzes title',
            'content': 'Quizzes content',
            'photo': 'Quizzes image',
            'is_publ': 'Quizzes published',
            'publ_d_time': 'Quizzes published datetime',
        }
        widgets = {
            'content': forms.Textarea(attrs={'type': 'html'}),
            # 'q_person': forms.HiddenInput(),
        }
