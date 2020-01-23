from django.shortcuts import render
from .models import Article,Project
from django.views import generic
from django.contrib.auth import logout

# Create your views here.
class ArticleListView(generic.ListView):
    model = Article
    context_object_name = 'model'
    template_name = 'article_list.html'
    paginate_by=6

class ProjectListView(generic.ListView):
    model = Project
    context_object_name = 'model'
    template_name = 'project_list.html'
    paginate_by=6

def about(request):
    return render(
        request,
        'about.html'
    )

def logout_user(request):
    logout(request)
    return render(
        request,
        'registration/my_logout.html'
    )




