"""Athena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import PostListView, PostDetailView, ResumeListView
from django.contrib import admin

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='post-detail'),
    url(r'^resume', ResumeListView.as_view(), name='resume'),
    url(r'^xadmin/', admin.site.urls),
]

# change admin title and header

admin.site.site_header = 'He Xiangyu Blog. Administration'
admin.site.site_title = 'He Xiangyu Blog. Administration'
