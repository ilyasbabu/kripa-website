from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    date = models.DateTimeField()
    def __str__(self):
        return self.title
