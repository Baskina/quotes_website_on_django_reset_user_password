from django.db import models
from django.utils import timezone


class Author(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.fullname}"
