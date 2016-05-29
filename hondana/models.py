from django.db import models


class Book(models.Model):
    isbn_code = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    translator = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField()
    revision_date = models.DateField(blank=True, null=True)
