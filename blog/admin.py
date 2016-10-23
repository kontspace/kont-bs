from django.contrib import admin
from .models import Post, Category
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class PostProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'updated_at', 'created_at', 'post_file')
    list_filter = ('category', 'created_at')

admin.site.register(Post, PostProfileAdmin)
admin.site.register(Category)

admin.site.unregister(User)
admin.site.unregister(Group)
