from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_user_card, name='show_user_card'),
    path('<str:user_name>', views.show_user_card, name='show_user_card'),
]
