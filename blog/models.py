#!/usr/bin/env python
# coding:utf-8

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(u'类别名字', max_length=200)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(u'文章标题', max_length=200, help_text=u'文章标题')
    created_at = models.DateTimeField('创建日期', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改日期', auto_now=True)
    post_file = models.FileField(u'文件', upload_to='upload')
    category = models.ForeignKey(Category, related_name='post', null=True, blank=True)
    views = models.IntegerField(u'阅读数量', default=0, editable=False)

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return self.title

