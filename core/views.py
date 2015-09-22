from django.shortcuts import render

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class QuestionCreateView(CreateView):
    model = Question
    template_name = "question/question_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('success')

from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "home.html"

class Success(TemplateView):
  template_name = "success.html"