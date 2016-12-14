from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Post, Category
from collections import OrderedDict as _OrderedDict

import yaml
import os

CONFIGFILE = os.path.join(settings.BASE_DIR, 'config.yml')


def get_category_numbers():
    _categories = Category.objects.all().values_list('name')
    categories = map(lambda x: x[0], _categories)

    categories_numbers = _OrderedDict({'all': Post.objects.all().count()})
    categories_numbers.update({x: Post.objects.filter(category__name=x).count() for x in categories})
    return categories_numbers


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_default_context(self, **kwargs):
        return super(PostListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        query_values = self.request.GET.get('category', 'all')

        category = Post.objects.all() \
            if query_values == 'all' \
            else Post.objects.filter(category__name=query_values.title())
        return category

    def get_context_data(self, **kwargs):
        context = self.get_default_context(**kwargs)

        with open(CONFIGFILE) as f:
            context['info'] = yaml.safe_load(f)

        context['categories'] = get_category_numbers()
        context['title'] = 'Athena'
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['file_content'] = kwargs['object'].post_file.read()
        context['title'] = kwargs['object'].title
        return context

    def get_object(self):
        object = super(PostDetailView, self).get_object()
        object.views += 1
        object.save()
        return object
