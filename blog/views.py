from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
