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
from django.urls import path  # , include
from django.conf.urls import include, url

from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog, set_language
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema
from django.contrib.sitemaps.views import sitemap

from .views import (
    QuizzesIndexView,
    QuizzesDetailView,
    QuizzesView,
    QuestionView,
    QuizzesEnter,
    handle_404,
    handle_500,
)
from .api import api1

handler404 = handle_404
handler500 = handle_500

non_translatable_urlpatterns = [
    path("api1/", api1.urls),
    path('admin/', admin.site.urls),
    url(r'^i18n/$', set_language, name='set_language'),
    path('', QuizzesIndexView.as_view(), name='start'),
]
translatable_urlpatterns = [
    path('', QuizzesIndexView.as_view(), name='home'),
    path('quizzes/', QuizzesView.as_view(), name='add_quizzes'),
    path('quizzes/<int:pk>', QuizzesDetailView.as_view(), name='view_quizzes'),
    path('quizzes/edit/<int:pk>', QuizzesView.as_view(), name='edit_quizzes'),
    path('enter_quizzes/<int:pk>', QuizzesEnter.as_view(), name='enter_quizzes'),
    path('quizzes/<int:quizzes_id>/question/', QuestionView.as_view(), name='add_question'),
    path('accounts/', include('allauth.urls')),
    path('usercards/', include('usercards.urls')),
]

urlpatterns = non_translatable_urlpatterns + i18n_patterns(
    *translatable_urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
                      path('__debug__/',
                           include(debug_toolbar.urls)
                           ),
        ]
