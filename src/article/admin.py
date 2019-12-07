from django.contrib import admin
from .models import Article, Comment, Like, ArticleViews
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(ArticleViews)