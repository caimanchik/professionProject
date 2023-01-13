from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from web_profession.models import AboutParagraph


# Create your views here.

class MainView(ListView):

    model = AboutParagraph
    template_name = 'main.html'
