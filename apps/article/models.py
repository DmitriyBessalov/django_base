from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=512, unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
