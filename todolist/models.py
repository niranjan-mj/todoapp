import datetime

from django import forms
from django.db import models

from django.utils import timezone



class TodoList(models.Model):
    author = models.CharField(max_length=50, blank= True)
    description = models.TextField(max_length=200)
    title = models.CharField(max_length=100)
    # content = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title