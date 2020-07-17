from django import forms
from django.contrib.auth.models import User
from .models import UserCard


class User(forms.ModelForm):
    """Form for the User model"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserCard(forms.ModelForm):
    """Form for the UserCard model"""
    def __init__(self,*args,**kwargs):
        self.person_id = kwargs.pop('person_id')
        super(UserCard,self).__init__(*args,**kwargs)

    class Meta:
        model = UserCard
        fields = ('about', 'birthday', 'photo')
        # exclude = ('user', )
