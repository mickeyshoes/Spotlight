from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    GENDER = (
        ('M','남자'),
        ('W','여자'),
    )
    birthday = models.DateField(blank = True, null = True) # 둘다 True인 경우 -> 로그인에 상관이 없는 경우
    gender = models.CharField(max_length=2,blank = True, null = True,choices=GENDER)

# Create your models here.
