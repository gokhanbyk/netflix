from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length= 30)
    image = models.FileField(upload_to='profile_pic')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from = 'name', unique=True, null=True)

    def __str__(self):
        return self.name