
from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    def __str__(self):
        return self.tag

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    relations = models.ManyToManyField("self", blank=True)
    def __str__(self):
        return self.title
