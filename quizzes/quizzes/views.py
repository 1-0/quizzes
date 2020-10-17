from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.i18n import set_language
from django.views.generic.edit import FormView
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.utils.translation import activate, get_language_from_request, get_supported_language_variant, override
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language, get_language,
)
from django.conf import settings
from .models import Quizzes, Question, FS
from .forms import QuizzesForm, QuestionForm, EnterQuizzesForm


class Home(FormView):
    """Home - view class for home page"""
    model_class = Quizzes
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        lang_code = get_supported_language_variant(get_language_from_request(request))
        override(lang_code)

        quizzes_all = self.model_class.objects.all().order_by('publ_d_time').reverse()
        paginator = Paginator(quizzes_all, 10)
        page_number = request.GET.get('page')
        quizzes_list = paginator.get_page(page_number)
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
        if not quizzes_id and not request.user.id:
            return redirect(r'/')
        if quizzes_id:
            quizzes = get_object_or_404(self.model_class, pk=quizzes_id)
            form = self.form_class(instance=quizzes)
        else:
            quizzes = self.model_class()
            form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'quizzes': quizzes,
                'quizzes_id': quizzes_id,
            },
        )

    def post(self, request, quizzes_id=None, *args, **kwargs):
        photo_quizzes = None
        if quizzes_id:
            quizzes = self.model_class.objects.get(pk=quizzes_id)
        else:
            quizzes = self.model_class()
        form = self.form_class(
            request.POST or None,
            request.FILES or None,
            instance=quizzes
        )
        if quizzes.photo.name:
            old_file = quizzes.photo.name
        else:
            old_file = None
        if form.is_valid():
            if len(request.FILES) > 0:
                photo_quizzes = request.FILES.get('photo', None)
                photo_quizzes.name = '.'.join([request.user.username, photo_quizzes.name.split('.')[-1]])
            if form.save():
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    _('Quizzes Data is saved')
                )
                if len(request.FILES) > 0 and photo_quizzes and old_file:
                    FS.delete(old_file)
            else:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    _('Quizzes Data is not saved')
                )
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'quizzes': quizzes,
                'quizzes_id': quizzes_id,
            },
        )


class QuestionView(LoginRequiredMixin, FormView):
    """QuestionView - view class for question view page"""

    login_url = '/accounts/login/'
    model_class = Question
    form_class = QuestionForm
    template_name = r"quizzes/question_model_form.html"

    def get(self, request, quizzes_id=None, question_id=None, *args, **kwargs):
        if not question_id and not quizzes_id:
            return redirect(r'/')
        if quizzes_id and question_id:
            question = get_object_or_404(self.model_class, pk=question_id)
            form = self.form_class(instance=question)
        else:
            question = self.model_class()
            form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'question': question,
                'quizzes_id': quizzes_id,
                'question_id': question_id,
            },
        )

    def post(self, request, quizzes_id=None, question_id=None, *args, **kwargs):
        photo_question = None
        if question_id:
            question = self.model_class.objects.get(pk=question_id)
        else:
            question = self.model_class()
        form = self.form_class(
            request.POST or None,
            request.FILES or None,
            instance=question
        )
        if question.photo.name:
            old_file = question.photo.name
        else:
            old_file = None
        if len(request.FILES) > 0:
            photo_question = request.FILES.get('photo', None)
            photo_question.name = '.'.join([request.user.username, photo_question.name.split('.')[-1]])
        if form.is_valid():
            if form.save():
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    _('Question Data is saved')
                )
                if len(request.FILES) > 0 and photo_question and old_file:
                    FS.delete(old_file)
            else:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    _('Question Data is not saved')
                )
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'question': question,
                'quizzes_id': quizzes_id,
                'question_id': question_id,
            },
        )


class QuizzesEnter(LoginRequiredMixin, FormView):
    """QuizzesEnter - view class for enter quizzes view page"""

    login_url = '/accounts/login/'
    model_class = Quizzes
    form_class = EnterQuizzesForm
    template_name = r"quizzes/enter_quizzes_form.html"

    def get(self, request, quizzes_id=None, *args, **kwargs):
        quizzes = get_object_or_404(self.model_class, pk=quizzes_id)
        form = self.form_class(instance=quizzes)
        return HttpResponse('''enter_quizzes %s <br> form %s''' % (quizzes.id, form.fields))

# form ['Meta', '__class__', '__delattr__',
#       '__dict__', '__dir__', '__doc__', '__eq__',
#       '__format__', '__ge__', '__getattribute__',
#       '__getitem__', '__gt__', '__hash__',
#       '__html__', '__init__', '__init_subclass__',
#       '__iter__', '__le__', '__lt__', '__module__',
#       '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#       '__repr__', '__setattr__', '__sizeof__',
#       '__str__', '__subclasshook__', '__weakref__',
#       '_bound_fields_cache', '_clean_fields', '_clean_form',
#       '_errors', '_get_validation_exclusions', '_html_output',
#       '_meta', '_post_clean', '_save_m2m', '_update_errors',
#       '_validate_unique', 'add_error', 'add_initial_prefix',
#       'add_prefix', 'as_p', 'as_table', 'as_ul', 'auto_id',
#       'base_fields', 'changed_data', 'clean', 'data', 'declared_fields',
#       'default_renderer', 'empty_permitted', 'error_class',
#       'errors', 'field_order', 'fields', 'files', 'full_clean',
#       'get_initial_for_field', 'has_changed', 'has_error', 'hidden_fields',
#       'initial', 'instance', 'is_bound', 'is_multipart', 'is_valid',
#       'label_suffix', 'media', 'non_field_errors', 'order_fields',
#       'prefix', 'renderer', 'save', 'use_required_attribute',
#       'validate_unique', 'visible_fields']


def handle_404(request, exception=None):
    return TemplateResponse(request, '404.html', status=404)


def handle_500(request, exception=None):
    return TemplateResponse(request, '500.html', status=500)

