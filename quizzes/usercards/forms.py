from django import forms
from django.contrib.auth.models import User
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
            'first_name': 'First name',
            'last_name': 'Last Name',
            'email': 'E-mail',
            'date_joined': 'Date Joined',
        }


class UserCard(forms.ModelForm):

    class Meta:
        model = UserCard
        fields = ('about', 'birthday', 'photo')
        labels = {
            'about': 'About',
            'birthday': 'Birthday',
            'photo': 'Photo',
        }
        widgets = {
            'about': forms.Textarea(attrs={'type': 'html'}),
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
