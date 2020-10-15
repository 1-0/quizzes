from django import forms
from django.utils.translation import gettext as _
from .models import Quizzes, Question, Answer


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('content', 'photo', 'correct')
        labels = {
            'content': _('Answer content'),
            'photo': _('Answer image'),
            'correct': _('Correct answer'),
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
            'content': _('Question content'),
            'photo': _('Question image'),
        }
        widgets = {
            'content': forms.Textarea(attrs={'type': 'html'}),
        }


class QuizzesForm(forms.ModelForm):
    is_publ = forms.BooleanField(
        required=False,
        label=_('Published'),
        widget=forms.CheckboxInput(attrs={'class': 'filled-in'}),
        initial=False,
    )
    # ordering = ['-publ_d_time', 'title']
    ordering = ['-id']
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
            'title': _('Quizzes title'),
            'content': _('Quizzes content'),
            'photo': _('Quizzes image'),
            'is_publ': _('Quizzes published'),
            'publ_d_time': _('Quizzes published datetime'),
        }
        widgets = {
            'content': forms.Textarea(attrs={'type': 'html'}),
            # 'q_person': forms.HiddenInput(),
        }
