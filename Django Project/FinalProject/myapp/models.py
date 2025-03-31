from django.db import models

# Create your models here.


class userSignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    password = models.CharField(max_length=12)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    photo = models.ImageField(upload_to="Photos")
