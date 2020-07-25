from django.db import models

# Create your models here.

class MovieInfo(models.Model):
    movieTitle = models.CharField(max_length = 50)
    movieGenre = models.CharField(max_length=10, unique=True)
    movieImage = models.ImageField(upload_to="images/", blank=True)
    