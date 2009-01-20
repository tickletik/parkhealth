from django.db import models


# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


class Photo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField()

    thumb = models.ImageField(upload_to='uploads/gallery/thumbs/')
    large = models.ImageField(upload_to='uploads/gallery/large/')

    gallery = models.ForeignKey('PhotoGallery')

