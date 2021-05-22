from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
LEVEL_CHOICES=((1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9))
ITEM_CHOICES1=((0,0),
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9))
ITEM_CHOICES2=((0,0),
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9))
ITEM_CHOICES=((0,0),
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9))
class Profile(models.Model):
    first=models.CharField(max_length=100,blank=False,null=False)
    last=models.CharField(max_length=100,blank=False,null=False)
    img=models.ImageField(default="enviro.png",upload_to="/profilepics")
    email=models.EmailField(max_length=200,blank=True)
    bio=models.TextField(default="Save Earth!",blank=True)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    country=models.CharField(max_length=200,blank=True)
class Level(models.Model):
    user=models.OneToOneField(Profile,on_delete=models.CASCADE)
    number=models.IntegerField(default=1,choices=LEVEL_CHOICES)
    
class PointWorth(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    points=models.IntegerField(default=0)


class Reduce(models.Model):
    user_reduce=models.OneToOneField(Profile,on_delete=models.CASCADE)
    filled_reduce=models.IntegerField(default=0,choices=ITEM_CHOICES1)
    text_reduce=models.ArrayField(models.TextField(max_length=400))
class Reuse(models.Model):
    user_reuse=models.OneToOneField(Profile,on_delete=models.CASCADE)
    filled_reuse=models.IntegerField(default=0,choices=ITEM_CHOICES2)
    text_reuse=models.ArrayField(models.TextField(max_length=400))
class Recycle(models.Model):
    user_recycle=models.OneToOneField(Profile,on_delete=models.CASCADE)
    filled_recycle=models.IntegerField(default=0,choices=ITEM_CHOICES)
    text_recycle=models.ArrayField(models.TextField(max_length=400))
