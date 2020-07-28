from django.db import models
from main.models import MovieInfo
from django.conf import settings
from django.contrib.auth.models import User


class Comment(models.Model):
    movie = models.ForeignKey(MovieInfo, on_delete=models.CASCADE)
    spo_review = models.BooleanField()
    grade = models.IntegerField(null=True, default=0)
    comment_body = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.ManyToManyField(User,related_name='likers')

