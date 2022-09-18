from csv import list_dialects
from django.contrib import admin
from .models import Author, Tag, Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'title', 'tags')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'email', 'date')


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
