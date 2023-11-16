from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from = 'name')

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from = 'name')

    def __str__(self):
        return self.name


class Movies(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    image = models.FileField(upload_to='movie_pic')
    slug = AutoSlugField(populate_from = 'name')
    video = models.FileField(upload_to='movie_video')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name