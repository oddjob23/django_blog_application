from django.contrib import admin
from .models import Article, Comment, Like, ArticleViews
# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(ArticleViews)