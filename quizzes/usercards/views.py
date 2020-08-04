from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
# from .forms import UserInfo, UserCard, UserForm
from .models import UserCard as UCard


@login_required
def show_user(request, user_name):
    """show_user - show user page"""
    forms = []
    valid_user = False
    try:
        user = User.objects.get(username=user_name)
    except:
        user = User()
    try:
        user_data = UCard.objects.get(person_id=user.id)
    except:
        user_data = UCard()
    forms.append(UserAll(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'date_joined': user.date_joined,
    }))
    forms.append(UserCardAll(initial={
        'about': user_data.about,
        'birthday': user_data.birthday,
        'photo': user_data.photo,
    }))
    if request.method == 'GET':
        if user_name == request.user.get_username():
            valid_user = user_name
        else:
            for i in forms:
                for f in i.fields:
                    i.fields[f].disabled = True
    elif request.method == 'POST':
        if user_name == request.user.get_username():
            valid_user = user_name
            form0 = UserAll(request.POST or None, request.FILES or None, instance=user)
            form1 = UserCardAll(request.POST or None, request.FILES or None, instance=user_data)
            saved_form = []
            if form0.is_valid():
                if form0.save():
                    saved_form.append(0)
                    forms[0] = form0
            if form1.is_valid():
                if form1.save():
                    saved_form.append(1)
                    forms[1] = form1
            if saved_form:
                messages.add_message(request, messages.SUCCESS, 'Data is saved')
            else:
                messages.add_message(request, messages.SUCCESS, 'Data is not saved')

    return render(
        request,
        'usercards/show_user.html',
        {
            'user_data': user_data,
            'user_name': user_name,
            'valid_user': valid_user,
            'forms': forms,
        }
    )

