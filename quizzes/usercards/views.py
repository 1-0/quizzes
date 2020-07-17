from django.shortcuts import render
from .forms import User, UserCard


def show_user_card(request, user_name):
    """show_user_card - show user card page"""
    if request.method == 'POST' or request.method == 'GET':
        if user_name == request.user.get_username():
            valid_user = user_name
            form = UserCard(request.POST, request.FILES, person_id = user_name)
            if form.is_valid():
                form.save()
                # Get the current instance object to display in the template
                img_obj = form.instance
                return render(
                    request,
                    'usercards/show_user_card.html',
                    {
                        'valid_user': valid_user,
                        'form': form,
                        'img_obj': img_obj
                    }
                )
            else:
                form = UserCard(person_id = user_name)
            return render(
                request,
                'usercards/show_user_card.html',
                {
                    'valid_user': valid_user,
                    'form': form
                }
            )
        else:
            form = UserCard(person_id = user_name)
            valid_user = False
        return render(
            request,
            'usercards/show_user_card.html',
            {
                'valid_user': valid_user,
                'form': form
            }
        )


def show_user_data(request, user_name):
    """show_user_data - show user data page"""
    if request.method == 'POST' or request.method == 'GET':
        if user_name == request.user.get_username():
            valid_user = user_name
            form = User(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Get the current instance object to display in the template
                img_obj = form.instance
                return render(
                    request,
                    'usercards/show_user_card.html',
                    {
                        'valid_user': valid_user,
                        'form': form,
                        'img_obj': img_obj
                    }
                )
            else:
                form = User()
            return render(
                request,
                'usercards/show_user_card.html',
                {
                    'valid_user': valid_user,
                    'form': form
                }
            )
        else:
            form = User()
            valid_user = False
        return render(
            request,
            'usercards/show_user_card.html',
            {
                'valid_user': valid_user,
                'form': form
            }
        )
