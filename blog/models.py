from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from .utils import unique_slugify
# Create your models here.

REACH_CHOICES = [
    ('featured' , 'Featured'),
    ('normal','Normal')
]

class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    slug = models.SlugField(max_length=300 , unique=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    reach = models.CharField(max_length=20, choices=REACH_CHOICES , default='normal')

    class Meta:
        ordering = ['-created']

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self , slugify(self.title))
        super().save(*args , **kwargs)

    def __str__(self):
        return str(self.title + " by " + self.author.username)
    
class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Comment by " + self.author.username + " on  " + self.post.title