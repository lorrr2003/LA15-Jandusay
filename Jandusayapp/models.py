from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
