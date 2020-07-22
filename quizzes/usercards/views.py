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


def prepare_formset_user(user, user_data):
    UserDataFormSet1 = formset_factory(UserInfo, extra=2)
    formset1 = UserDataFormSet1(initial=[
        {
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
    ])
    UserCardFormSet2 = formset_factory(UserCard, extra=2)
    formset2 = UserCardFormSet2(initial=[
        {
            'about': user_data.about,
            'birthday': user_data.birthday,
        }
    ])
    formset = [formset1, formset2]
    return formset


@login_required
def show_user(request, user_name):
    """show_user - show user page"""
    formset = None
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
            formset = prepare_formset_user(user, user_data)
            valid_user = user_name
        else:
            valid_user = False
    elif request.method == 'POST':
        if user_name == request.user.get_username():
            valid_user = user_name
            form1 = UserInfo(request.POST)
            form2 = UserCard(request.POST)
            if form1.is_valid():
                user_data.first_name = form.data['form-0-first_name']
                user_data.last_name = form.data['form-0-last_name']
                user_data.save()
                messages.add_message(request, messages.SUCCESS, 'Data1 saved')
            if form2.is_valid():
                user_data.about = form.data['form-1-about']
                user_data.birthday = form.data['form-1-birthday']
                user_data.save()
                messages.add_message(request, messages.SUCCESS, 'Data2 saved')
                # form.save()
            # formset = [form1, form2]
            formset = prepare_formset_user(user, user_data)
    return render(
        request,
        'usercards/show_user_card.html',
        {
            'user': user,
            'user_data': user_data,
            'user_name': user_name,
            'valid_user': valid_user,
            'form': form,
            'formset': formset,
        }
    )


def show_user_card(request, user_name):
    """show_user_card - show user card page"""
    form = None
    formset = None
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
            form1 = prepare_form_usercard(user_data)
            form2 = prepare_form_usercard(user_data)
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
            'form': form,
            'form1': form1,
            'form2': form2,
            'formset': formset,
        }
    )


@login_required
def show_user_data(request, user_name):
    """show_user_data - show user data page"""
    formset = None
    form = None
    valid_user = False
    try:
        user_data = User.objects.get(username=user_name)
    except:
        user_data = User()
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
            'form': form,
            'formset': formset,
        }
    )

