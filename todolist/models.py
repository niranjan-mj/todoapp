from django.db import models

from django.utils import timezone



class TodoList(models.Model):
    author = models.CharField(max_length=50, blank= True)
    description = models.TextField(max_length=200)
    title = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(default=timezone.now())
    due_date = models.DateField()
