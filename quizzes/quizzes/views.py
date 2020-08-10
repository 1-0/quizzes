# views.py
from django.views.generic import TemplateView

from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import QuizzesForm


class Home(TemplateView):
    """Home - view class for home page"""
    template_name = 'home.html'


class QuizzesFormView(FormView):
    form_class = QuizzesForm

    template_name = r"quizzes/quizzes_model_form.html"

    success_url = r"/"

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, QuizzesFormView.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return redirect('/')

        return render(request, self.template_name, {'form': form})

