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
    if request.method == 'GET':
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
        if user_name == request.user.get_username():
            valid_user = user_name
        else:
            for i in forms.fields:
                for f in i:
                    i.fields[f].disabled = True
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


@login_required
def show_user_all(request, user_name):
    """show_user_all - show user data page"""
    valid_user = False
    try:
        user_data = User.objects.get(username=user_name)
    except:
        user_data = UserAll()
    if request.method == 'GET':
        form = UserAll(initial={
            'first_name': user_data.first_name,
            'last_name': user_data.last_name,
            'email': user_data.email,
            'date_joined': user_data.date_joined,
        })
        if user_name == request.user.get_username():
            valid_user = user_name
        else:
            for f in form.fields:
                form.fields[f].disabled = True
    elif request.method == 'POST':
        if user_name == request.user.get_username():
            valid_user = user_name
            form = UserAll(request.POST or None, request.FILES or None, instance=user_data)
            if form.is_valid():
                if form.save():
                    messages.add_message(request, messages.SUCCESS, 'Data saved')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Valid Data not saved')
            else:
                messages.add_message(request, messages.SUCCESS, 'Not Valid Data not saved')
    return render(
        request,
        'usercards/show_user_all.html',
        {
            'user_data': user_data,
            'user_name': user_name,
            'valid_user': valid_user,
            'form': form,
        }
    )


@login_required
def show_user_card_all(request, user_name):
    """show_user_card_all - show user card data page"""
    form = None
    valid_user = False
    try:
        user = User.objects.get(username=user_name)
    except:
        user = User()
    try:
        user_data = UCard.objects.get(person_id=user.id)
    except:
        user_data = UCard()
    if request.method == 'GET':
        form = UserCardAll(initial={
            'about': user_data.about,
            'birthday': user_data.birthday,
            'photo': user_data.photo,
        })
        if user_name == request.user.get_username():
            valid_user = user_name
        else:
            for f in form.fields:
                form.fields[f].disabled = True
    elif request.method == 'POST':
        if user_name == request.user.get_username():
            valid_user = user_name
            form = UserCardAll(request.POST or None, request.FILES or None, instance=user_data)
            if form.is_valid():
                if form.save():
                    messages.add_message(request, messages.SUCCESS, 'Data saved')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Valid Data not saved')
            else:
                messages.add_message(request, messages.SUCCESS, 'Not Valid Data not saved')
    return render(
        request,
        'usercards/show_user_card_all.html',
        {
            'user_data': user_data,
            'user_name': user_name,
            'valid_user': valid_user,
            'form': form,
        }
    )

