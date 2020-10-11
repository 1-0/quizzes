"""quizzes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema

from .views import Home, QuizzesView, QuestionView, hello
from .api import api1

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('hello', hello, name='hello'),
    path('admin/', admin.site.urls),
    path('quizzes/', QuizzesView.as_view(), name='add_quizzes'),
    path('quizzes/<int:quizzes_id>', QuizzesView.as_view(), name='view_quizzes'),
    path('quizzes/<int:quizzes_id>/question/', QuestionView.as_view(), name='add_question'),
    path('accounts/', include('allauth.urls')),
    path('usercards/', include('usercards.urls')),
    path("api1/", api1.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = [
                      path('__debug__/',
                           include(debug_toolbar.urls)
                           ),
        ] + urlpatterns
