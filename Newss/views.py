from django.shortcuts import render
from .models import News
import requests
from django.views.generic import ListView,TemplateView,DetailView

class index(TemplateView):
      template_name = "index.html"

class NewsList(ListView):
    model = News
    template_name = "home.html"
    context_object_name='news'

class NewsDetail(DetailView):
    model = News
    template_name = "detail.html"
    context_object_name='ndetail'
    
     