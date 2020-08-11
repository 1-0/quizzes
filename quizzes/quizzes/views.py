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

        quizzes_list = self.model_class.objects.all()
        return render(
            request,
            self.template_name,
            {'quizzes_list': quizzes_list},
        )

class QuizzesView(FormView):

    model_class = Quizzes
    form_class = QuizzesForm
    template_name = r"quizzes/quizzes_model_form.html"
    # success_url = r"/"

    def get(self, request, quizzes_id=None, *args, **kwargs):
        if quizzes_id:
            quizzes = self.model_class.objects.get(pk=quizzes_id)
            if request.user:
                form = self.form_class(initial={
                    'title': quizzes.title,
                    'person': quizzes.person,
                    'content': quizzes.content,
                    'image': quizzes.image,
                    'published': quizzes.published,
                    'published_datetime': quizzes.published_datetime,
                })
            else:
                return redirect(r'/')
        else:
            quizzes = self.model_class()
            if request.user:
                form = self.form_class()
            else:
                return redirect(r'/')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'quizzes': quizzes,
            },
        )

    def post(self, request, quizzes_id=None, *args, **kwargs):
        if quizzes_id:
            quizzes = self.model_class.objects.get(pk=quizzes_id)
        else:
            quizzes = self.model_class()
        # quizzes = self.model_class.objects.get(pk=quizzes_id)
        form = self.form_class(
            request.POST or None,
            request.FILES or None,
            instance=quizzes
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
            {
                'form': form,
                'quizzes': quizzes,
            },
        )
