from django import forms
# from django.forms import modelform_factory, EmailField, DateTimeField
# from django.forms.widgets import Textarea, TextInput, FileInput, DateInput, EmailInput, DateTimeInput
from django.contrib.auth.models import User
from .models import UserCard


class UserAll(forms.ModelForm):

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
        help_texts = {
            'first_name': 'Enter first name',
            'last_name': 'Enter last name',
        }


class UserCardAll(forms.ModelForm):

    class Meta:
        model = UserCard
        fields = ('about', 'birthday')
        # fields = ('about', 'birthday', 'photo'),
        labels = {
            'about': 'About',
            'birthday': 'Birthday',
            # 'photo': 'Photo',
        }
        help_texts = {
            'about': 'Enter about',
            'birthday': 'Enter birthday',
        }
        widgets = {
            'about': forms.Textarea(attrs={'type': 'html'}),
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


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


class UserForm(forms.Form):
    """UserForm = Form for the user"""
    first_name = forms.CharField(max_length=200, widget=forms.TextInput)
    last_name = forms.CharField(max_length=200, widget=forms.TextInput)
    about = forms.CharField(widget=forms.Textarea)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    photo = forms.ImageField()
