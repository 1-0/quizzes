from django.urls import path

from . import views

urlpatterns = [
    path('show_user/<str:user_name>', views.show_user, name='show_user'),
    path('show_user_all/<str:user_name>', views.show_user_all, name='show_user_all'),
    path('show_user_card_all/<str:user_name>', views.show_user_card_all, name='show_user_card_all'),
]
