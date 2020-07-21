from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserInfo, UserCard
from .models import UserCard as UCard


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


def show_user(request, user_name):
    """show_user - show user page"""
    form = None
    try:
        user = User.objects.get(username=user_name)
    except:
        user = User()
    try:
        user_data = UCard.objects.get(person=user)
    except:
        user_data = UCard()
    if request.method == 'GET':
        if user_name == request.user.get_username():
            form = prepare_form_usercard(user_data)
            valid_user = user_name
        else:
            valid_user = False
    elif request.method == 'POST':
        if user_name == request.user.get_username():
            valid_user = user_name
            form = UserCard(request.POST)
            if form.is_valid():
                user_data.about = form.data['form-0-about']
                user_data.birthday = form.data['form-0-birthday']
                user_data.save()
                messages.add_message(request, messages.SUCCESS, 'Data saved')
                # form.save()
            form = prepare_form_usercard(user_data)
    return render(
        request,
        'usercards/show_user_card.html',
        {
            'user': user,
            'user_data': user_data,
            'user_name': user_name,
            'valid_user': valid_user,
            'form': form
        }
    )


def show_user_card(request, user_name):
    """show_user_card - show user card page"""
    form = None
    try:
        user = User.objects.get(username=user_name)
    except:
        user = User()
    try:
        user_data = UCard.objects.get(person=user)
    except:
        user_data = UCard()
    if request.method == 'GET':
        if user_name == request.user.get_username():
            form = prepare_form_usercard(user_data)
            valid_user = user_name
        else:
            valid_user = False
    elif request.method == 'POST':
        if user_name == request.user.get_username():
            valid_user = user_name
            form = UserCard(request.POST)
            if form.is_valid():
                user_data.about = form.data['form-0-about']
                user_data.birthday = form.data['form-0-birthday']
                user_data.save()
                messages.add_message(request, messages.SUCCESS, 'Data saved')
                # form.save()
            form = prepare_form_usercard(user_data)
    return render(
        request,
        'usercards/show_user_card.html',
        {
            'user_data': user_data,
            'user_name': user_name,
            'valid_user': valid_user,
            'form': form
        }
    )


@login_required
def show_user_data(request, user_name):
    """show_user_data - show user data page"""
    form = None
    valid_user = False
    try:
        user_data = UCard.objects.get(person=user)
    except:
        user_data = UCard()
    if request.method == 'GET':
        if user_name == request.user.get_username():
            form = prepare_form_user_info(user_data)
            valid_user = user_name
    elif request.method == 'POST':
        if user_name == request.user.get_username():
            valid_user = user_name
            form = UserInfo(request.POST)
            if form.is_valid():
                user_data.first_name = form.data['form-0-first_name']
                user_data.last_name = form.data['form-0-last_name']
                user_data.save()
                # form.save()
            messages.add_message(request, messages.SUCCESS, 'Data saved')
            form = prepare_form_user_info(user_data)
    return render(
        request,
        'usercards/show_user_card.html',
        {
            'user_data': user_data,
            'user_name': user_name,
            'valid_user': valid_user,
            'form': form
        }
    )

