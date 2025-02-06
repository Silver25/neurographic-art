from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))  # constant

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # must be unique
    slug = models.SlugField(max_length=200, unique=True)  # must be unique
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="journal_posts"
)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
