from django.db import models
from main.models import MovieInfo


class Comment(models.Model):
    user_id = models.ForeignKey()
    movie = models.ForeignKey(MovieInfo, on_delete=models.CASCADE)
    spo_review = models.BooleanField()
    like = models.IntegerField(null=True, default=0)
    dislike = models.IntegerField(null=True, default=0)
    grade = models.IntegerField(null=True, default=0)
    comment_body = models.TextField()
