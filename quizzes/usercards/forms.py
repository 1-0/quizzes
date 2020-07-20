from django import forms
from django.contrib.auth.models import User
from .models import UserCard


class UserInfo(forms.ModelForm):
    """Form for the User model"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserCard(forms.ModelForm):
    """Form for the UserCard model"""
    class Meta:
        model = UserCard
        fields = ('about', 'birthday', 'photo')
        # exclude = ('user', )
