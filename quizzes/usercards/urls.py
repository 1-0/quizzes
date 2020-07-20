from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_user_card, name='show_user_card'),
    path('show_user_card/<str:user_name>', views.show_user_card, name='show_user_card'),
    path('show_user_data/<str:user_name>', views.show_user_data, name='show_user_data'),
    path('show_user/<str:user_name>', views.show_user, name='show_user'),
]
