from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=500)

    slug = models.CharField(max_length=500, editable=False)


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.TextField()

    is_published = models.BooleanField(default=False)

    slug = models.SlugField(max_length=500, editable=False)

    shared_to = models.ManyToManyField(Blog, related_name='shared_posts')