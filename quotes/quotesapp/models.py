from django.db import models
from django.utils import timezone

from authorsapp.models import Author


class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)


class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(default=timezone.now)
