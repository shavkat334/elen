from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from .models import Article, Profile, Category

class HomePageView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = "articles"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["blog_owner"] = User.objects.filter(is_superuser=True).latest("date_joinec")
        return context

    
      