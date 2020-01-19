from django.shortcuts import render
from django.views import generic
from .models import Article


# Create your views here.
class ArticleListView(generic.ListView):
    model = Article
    context_object_name = 'model'
    template_name = 'article_list.html'
    paginate_by=6

