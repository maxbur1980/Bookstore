from django.db import models


class Author(models.Model):
    nickname = models.CharField(max_length=100)
    was_born = models.DateField()

    def __str__(self):
        return self.nickname


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    length = models.IntegerField()
    published = models.DateField()

    def __str__(self):
        return self.title
