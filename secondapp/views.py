from django.shortcuts import render, HttpResponse
from secondapp.models import People, Article
from django.template import Template, Context
# Create your views here.
def index(requests):
    context = {}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    index_page = render(requests, 'index.html', context)
    return index_page
