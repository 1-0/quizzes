from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserInfo, UserCard
from .models import UserCard as UCard
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory


def show_user_card(request, user_name):
    """show_user_card - show user card page"""
    form = None
    if request.method == 'GET':
        u = User.objects.get(username=user_name)
        user_data = UCard.objects.get(person=u)
        if user_name == request.user.get_username():
            UserCardFormSet = formset_factory(UserCard, extra=2)
            formset = UserCardFormSet(initial=[
                {
                    'about': user_data.about,
                    'birthday': user_data.birthday,
                }
            ])
            form = formset[0]
            valid_user = user_name
        else:
            valid_user = False
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


def prepare_form_user(user_data):
    UserDataFormSet = formset_factory(UserInfo, extra=2)
    formset = UserDataFormSet(initial=[
        {
            'first_name': user_data.first_name,
            'last_name': user_data.last_name,
        }
    ])
    return formset[0]


@login_required
def show_user_data(request, user_name):
    """show_user_data - show user data page"""
    form = None
    valid_user = False
    user_data = User.objects.get(username=user_name)
    if request.method == 'GET':
        if user_name == request.user.get_username():
            # UserDataFormSet = formset_factory(UserInfo, extra=2)
            # formset = UserDataFormSet(initial=[
            #     {
            #         'first_name': user_data.first_name,
            #         'last_name': user_data.last_name,
            #     }
            # ])
            # form = formset[0]
            form = prepare_form_user(user_data)
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
            # UserDataFormSet = formset_factory(UserInfo, extra=2)
            # formset = UserDataFormSet(initial=[
            #     {
            #         'first_name': user_data.first_name,
            #         'last_name': user_data.last_name,
            #     }
            # ])
            # form = formset[0]
            form = prepare_form_user(user_data)
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

