from django.shortcuts import render
from .models import Project
from django.views import generic

# Create your views here.
class ProjectListView(generic.ListView):
    model = Project
    context_object_name = 'model'
    template_name = 'project_list.html'
    paginate_by=6