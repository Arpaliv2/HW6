from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

class NewsList(ListView):
    model = News
    ordering = '-time_of_addition'
    template_name = 'news.html'
    context_object_name = 'news_all'

class News_oneDetail(DetailView):
    model = News
    template_name = 'news_one.html'
    context_object_name = 'news'

# Create your views here.
