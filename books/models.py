from django.db import models

from authors.models import Author


class Book(models.Model):
    name = models.TextField(default='')
    edition = models.IntegerField(default=0)
    publication_year = models.IntegerField(default=0)
    authors = models.ManyToManyField(Author)
