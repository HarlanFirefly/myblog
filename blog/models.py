from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    modified_time = models.DateTimeField(auto_now=True, editable=False)
    excerpt = models.CharField(max_length=30, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']


class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.text[:20]
