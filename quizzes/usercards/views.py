from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserInfo, UserCard
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
    forms.append(UserInfo(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'date_joined': user.date_joined,
    }))
    forms.append(UserCard(initial={
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
            new_forms = []
            saved_form = []
            new_forms.append(UserInfo(
                request.POST or None,
                request.FILES or None,
                instance=user))
            new_forms.append(UserCard(
                request.POST or None,
                request.FILES or None,
                instance=user_data))
            for i in range(len(new_forms)):
                if new_forms[i].is_valid():
                    if new_forms[i].save():
                        saved_form.append(i)
                        forms[i] = new_forms[i]
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

