from django.contrib import admin
from .models import Post, Category, Resume
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class PostProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'updated_at', 'created_at', 'post_file')
    list_filter = ('category', 'created_at')


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'entry_time', 'time_of_separation')

admin.site.register(Post, PostProfileAdmin)
admin.site.register(Category)
admin.site.register(Resume, ResumeAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
