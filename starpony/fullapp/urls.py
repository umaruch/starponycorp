from django.urls import path,include
from . import views
from django.views.generic import RedirectView
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', RedirectView.as_view(url='/articles/',permanent=True)),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('about/',views.about,name='about'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('admin/', admin.site.urls),
]
