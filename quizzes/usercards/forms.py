from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .models import UserCard


class UserInfo(forms.ModelForm):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email'}),
        max_length=50,
        disabled=True
    )
    date_joined = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'email'}),
        disabled=True
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'date_joined')
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last Name'),
            'email': _('E-mail'),
            'date_joined': _('Date Joined'),
        }


class UserCard(forms.ModelForm):

    class Meta:
        model = UserCard
        fields = ('about', 'birthday', 'photo')
        labels = {
            'about': _('About'),
            'birthday': _('Birthday'),
            'photo': _('Photo'),
        }
        widgets = {
            'about': forms.Textarea(attrs={'type': 'html'}),
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
