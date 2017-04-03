#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.views.generic import ListView, DetailView
from django.shortcuts import render_to_response
from django.conf import settings
from .models import Post, Category, Resume, ContactInfo, Aboutme, OpenSourceProject, ContributedProject
from collections import OrderedDict as _OrderedDict

import yaml
import os

CONFIGFILE = os.path.join(settings.BASE_DIR, 'config.yml')

def get_meta_info():
    info = {}
    with open(CONFIGFILE) as f:
        info = yaml.safe_load(f)
    
    meta = {
       'GITHUB': os.getenv('GITHUB', None),
       'LINKED': os.getenv('LINKED', None),
       'EMAIL': os.getenv('EMAIL', None),
       'COPYRIGHT': os.getenv('COPYRIGHT', None),
    }

    for k, v in meta.items():
        if v != None:
            info[k] = v
        
    info['AD'] = os.getenv('AD', 'on')

    return info 

def get_category_numbers():
    _categories = Category.objects.all().values_list('name')
    categories = map(lambda x: x[0], _categories)

    categories_numbers = _OrderedDict({'all': Post.objects.all().count()})
    categories_numbers.update({x: Post.objects.filter(category__name=x).count() for x in categories})
    return categories_numbers

def get_contact_info():
    return ContactInfo.objects.all()

def get_aboutme():
    return Aboutme.objects.all()

def get_open_source_projects():
    return OpenSourceProject.objects.all()

def get_contributed_projects():
    return ContributedProject.objects.all()

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

        context['info'] = get_meta_info()
        context['categories'] = get_category_numbers()
        context['title'] = os.getenv('SITE_NAME', 'Athena')
        context['open_source_projects'] = get_open_source_projects()
        context['contributed_projects'] = get_contributed_projects()
        context['aboutme'] = get_aboutme()
        context['contact'] = get_contact_info()


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


class ResumeListView(ListView):
    model = Resume
    context_object_name = 'resumes'
    template_name = 'resume.html'

    def get_default_context(self, **kwargs):
        return super(ResumeListView, self).get_context_data(**kwargs)

    def get_context_data(self, **kwargs):
        context = self.get_default_context(**kwargs)
        context['title'] = 'Resume'
        return context

