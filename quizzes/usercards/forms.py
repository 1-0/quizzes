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
        fields = ('about', 'birthday')
        # fields = ('about', 'birthday', 'photo')
        # exclude = ('user', )


class UserForm(forms.Form):
    """UserForm = Form for the user"""
    first_name = forms.CharField(max_length=200, widget=forms.TextInput)
    last_name = forms.CharField(max_length=200, widget=forms.TextInput)
    about = forms.CharField(widget=forms.Textarea)
    # birthday = forms.DateField(widget=forms.Media)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    photo = forms.ImageField()
