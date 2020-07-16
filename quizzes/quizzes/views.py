# views.py
from django.views.generic import TemplateView


class Home(TemplateView):
    """Home - view class for home page"""
    template_name = 'home.html'