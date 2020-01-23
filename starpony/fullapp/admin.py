from django.contrib import admin
from .models import Article,Project
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('id','title','author','date')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=('id','title','author','date','status')
