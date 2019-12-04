from django.db import models

from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
# Create your models here.
Wrd = "World"
US = "U.S."
Tech = "Technology"
Des = "Design"
Cult = "Culture"
Bus = "Business"
Pol = "Politics"
Op = "Opinion"
Sc = "Science"
Hth = "Health"
St = "Style"
Tr = "Travel"
CATEGORY_CHOICES = (
    (Wrd, 'World'),
    (US, 'U.S.'),
    (Tech, 'Technology'),
    (Des, 'Design'),
    (Cult, 'Culture'),
    (Bus, 'Business'),
    (Pol, 'Politics'),
    (Op, 'Opinion'),
    (Sc, 'Science'),
    (Hth, 'Health'),
    (St, 'Style'),
    (Tr, 'Travel')
)
class Article(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=245, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    thumbnail = models.ImageField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    headline = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, default=Wrd, max_length=20)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        return super().save(*args, **kwargs)
    
    def get_headline_article(self):
        return Article.objects.filter(headline=True).last()
    

    # get all the comments
    @property
    def get_comments(self):
        return self.comments_set.all()
    # comment count -> comment_set.all().count()
    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    # like count
    @property
    def get_like_count(self):
        return self.like_set.all().count()
     # like url: for liking this specific post/article

     # used to make post request 
    def get_like_url(self):
        return reverse('like', kwargs={'slug': self.slug})
    # view count: count only unique views on this specific article
    @property
    def get_view_count(self):
        return self.postview_set.all().count()
    # get all the comments for this specific post
   

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

