from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(null=True, blank=True)
    completed = models.BooleanField(default=False)
