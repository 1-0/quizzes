from django.urls import path

from . import views

urlpatterns = [
    path('show_user/<str:user_name>', views.show_user, name='show_user'),
]
