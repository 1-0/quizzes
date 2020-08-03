from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
# from .forms import UserInfo, UserCard, UserForm
from .models import UserCard as UCard
import datetime


def prepare_form_user_info(user_data):
    UserDataFormSet = formset_factory(UserInfo, extra=2)
    formset = UserDataFormSet(initial=[
        {
            'first_name': user_data.first_name,
            'last_name': user_data.last_name,
        }
    ])
    return formset[0]


def prepare_form_usercard(user_data):
    UserCardFormSet = formset_factory(UserCard, extra=2)
    formset = UserCardFormSet(initial=[
        {
            'about': user_data.about,
            'birthday': user_data.birthday,
        }
    ])
    return formset[0]


def prepare_form_user(user_contribute, user_data):
    UserDataFormSet1 = formset_factory(UserForm)
    forms = UserDataFormSet1(initial=[
        {
            'first_name': user_contribute.first_name,
            'last_name': user_contribute.last_name,
            'about': user_data.about,
            'birthday': user_data.birthday,
        }
    ])
    return forms[0]


@login_required
def show_user(request, user_name):
    """show_user - show user page"""
    form = None
    valid_user = user_name
    try:
        user_contribute = User.objects.get(username=user_name)
    except:
        user_contribute = User()
    try:
        user_data = UCard.objects.get(person=user_contribute)
    except:
        user_data = UCard()
    if request.method == 'GET':
        if user_name == request.user.get_username():
            form = prepare_form_user(user_contribute, user_data)
        else:
            valid_user = False
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user_contribute.first_name = form.data['form-0-first_name']
            user_contribute.last_name = form.data['form-0-last_name']
            user_contribute.save()
            user_data.about = form.data['form-0-about']
            day = form.data['form-0-birthday'].split('-')
            user_data.birthday = datetime.date(int(day[0]), int(day[1]), int(day[2]))
            # user_data.birthday = form.data['form-0-birthday']
            user_data.save()
            user_name='valid '+form.data['form-0-first_name']+form.data['form-0-last_name']+form.data['form-0-about']+form.data['form-0-birthday']
            form = prepare_form_user(user_contribute, user_data)
            # form.save
        else:
            user_name = 'not valid '+form.data['form-0-first_name'] + form.data['form-0-last_name'] + form.data['form-0-about'] + \
                        form.data['form-0-birthday']

    return render(
        request,
        'usercards/show_user.html',
        {
            'user_contribute': user_contribute,
            'user_data': user_data,
            'user_name': user_name,
            'valid_user': valid_user,
            'form': form,
        }
    )


@login_required
def show_user_all(request, user_name):
    """show_user_data - show user data page"""
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
    """show_user_data - show user data page"""
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

