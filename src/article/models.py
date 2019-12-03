from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=245, null=True, blank=True)
    slug = models.SlugField(unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    thumbnail = models.ImageField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        return super().save(*args, **kwargs)

    # comment count

    # like count

    # view count: count only unique views on this specific article

    # get all the comments for this specific post
    # like url: for liking this specific post/article

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment[:50]

class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class ArticleViews(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

