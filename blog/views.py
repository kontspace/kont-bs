from django.views.generic import ListView, DetailView
from .models import Post

import info_config


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['info'] = info_config
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['file_content'] = kwargs['object'].post_file.read()
        return context

    def get_object(self):
        object = super(PostDetailView, self).get_object()
        object.views += 1
        object.save()
        return object
