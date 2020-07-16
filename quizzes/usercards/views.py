from django.shortcuts import render

def show_user_card(request, user_name):
    """show_user_card - show user card page"""
    if user_name==request.user.get_username():
        valid_user = user_name
    else:
        valid_user = False
    return render(request, 'usercards/show_user_card.html', {'valid_user': valid_user, })
