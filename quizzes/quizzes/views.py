from django.views.generic import TemplateView

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .models import Quizzes
from .forms import QuizzesForm


class Home(FormView):
    """Home - view class for home page"""
    model_class = Quizzes
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):

        quizzes_list = self.model_class.objects.all().order_by('published_datetime')
        return render(
            request,
            self.template_name,
            {'quizzes_list': quizzes_list},
        )


class NewQuizzes(FormView):
    form_class = QuizzesForm
    template_name = r"quizzes/quizzes_model_form.html"
    # success_url = r"/"

    # @login_required
    def get(self, request, *args, **kwargs):
        if request.user.is_active:
            form = self.form_class()
        else:
            return redirect(r'/')
        return render(
            request,
            self.template_name,
            {'form': form,},
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            request.POST or None,
            request.FILES or None,
        )
        if form.is_valid():
            if form.save():
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Quizzes Data is saved'
                )
            else:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Quizzes Data is not saved'
                )
        return render(
            request,
            self.template_name,
            {'form': form, },
        )


class QuizzesView(FormView):

    model_class = Quizzes
    form_class = QuizzesForm
    template_name = r"quizzes/quizzes_model_form.html"
    # success_url = r"/"

    def get(self, request, quizzes_id, *args, **kwargs):
        try:
            quizzes = self.model_class.objects.first()
        except:
            quizzes = self.model_class()

        if request.user:
            form = self.form_class(initial={
                'title': quizzes.title,
                'person': quizzes.person,
                'content': quizzes.content,
                'published': quizzes.published,
                'published_datetime': quizzes.published_datetime,
            })
        else:
            return redirect(r'/')
        return render(
            request,
            self.template_name,
            {'form': form,},
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            request.POST or None,
            request.FILES or None,
        )
        if form.is_valid():
            if form.save():
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Quizzes Data is saved'
                )
            else:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Quizzes Data is not saved'
                )
        return render(
            request,
            self.template_name,
            {'form': form, },
        )
