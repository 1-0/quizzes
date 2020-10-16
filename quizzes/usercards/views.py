import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from .forms import UserInfo, UserCard
from .models import FS
from .models import UserCard as UCard


logger = logging.getLogger(__name__)

@login_required
def show_user(request, user_name):
    """show_user - show user page"""
    forms = []
    valid_user = False
    user = get_object_or_404(User, username=user_name)
    try:
        user_data = UCard.objects.get(person_id=user.id)
    except:
        user_data = UCard()
    forms.append(UserInfo(instance=user))
    forms.append(UserCard(instance=user_data))
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
            old_file = user_data.photo.name
            if len(request.FILES) > 0:
                photo_user = request.FILES.get('photo', None)
                photo_user.name = '.'.join([user_name, photo_user.name.split('.')[-1]])

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
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    _('Data is saved')
                )
                if photo_user:
                    FS.delete(old_file)
            else:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    _('Data is not saved')
                )

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

