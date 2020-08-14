from django.views.generic import TemplateView

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .models import Quizzes, FS
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
    """QuizzesView - view class for quizzes view page"""

    model_class = Quizzes
    form_class = QuizzesForm
    template_name = r"quizzes/quizzes_model_form.html"
    readonly_fields = ('published_datetime',)

    def get(self, request, quizzes_id=None, *args, **kwargs):
        if quizzes_id:
            quizzes = self.model_class.objects.get(pk=quizzes_id)
            if request.user:
                form = self.form_class(instance=quizzes)
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
        form = self.form_class(
            request.POST or None,
            request.FILES or None,
            instance=quizzes
        )
        old_file = "" + quizzes.photo.name
        if form.is_valid():
            if len(request.FILES) > 0:
                # old_file = "" + quizzes.photo.name
                photo_quizzes = request.FILES.get('photo', None)
                photo_quizzes.name = '.'.join([request.user.username, photo_quizzes.name.split('.')[-1]])
            # request.FILES['photo'].photo.name = '_'.join([quizzes.id, request.FILES['photo'].photo.name])
            if form.save():
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Quizzes Data is saved'
                )
                # try:
                #     FS.delete(old_file)
                # except:
                #     pass
                # print(FS.url(quizzes.photo.name))
                if photo_quizzes:
                    FS.delete(old_file)
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
