from django.db import models

# Create your models here.
from user_api.models import User


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, unique=False)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
