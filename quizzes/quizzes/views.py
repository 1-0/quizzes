from django.views.generic import TemplateView

from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .models import Quizzes
from .forms import QuizzesForm


class MyClass:

    def __init__(self, *args, **kwargs):
        super(MyClass, self).__init__(*args, **kwargs)
        self.title = 't1'
        self.id = 1




# class Home(TemplateView):
#     """Home - view class for home page"""
#     template_name = 'home.html'

class Home(FormView):
    """Home - view class for home page"""
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):

        quizzes_list = [MyClass(), ]
        try:
            quizzes_list = Quizzes.objects.all()
        except:
            quizzes_list = [Quizzes(), ]
        return render(
            request,
            Home.template_name,
            {'quizzes_list': quizzes_list},
        )


class QuizzesFormView(FormView):
    form_class = QuizzesForm

    template_name = r"quizzes/quizzes_model_form.html"

    success_url = r"/"

    def get(self, request, quizzes_id, *args, **kwargs):
        try:
            quizzes_list = Quizzes.objects.all()
        except:
            quizzes_list = [Quizzes(), ]
        # forms.append(UserInfo(initial={
        #     'first_name': user.first_name,
        #     'last_name': user.last_name,
        #     'email': user.email,
        #     'date_joined': user.date_joined,
        # }))

        form = self.form_class
        quizzes_list = MyClass()
        return render(
            request,
            QuizzesFormView.template_name,
            {'form': form, 'quizzes_list': quizzes_list},
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return redirect('/')

        return render(request, self.template_name, {'form': form})

