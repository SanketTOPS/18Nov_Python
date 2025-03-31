from django.db import models


# Create your models here.
class mybill(models.Model):
    name = models.CharField(max_length=20)
    qty = models.IntegerField()
    price = models.IntegerField()
    total = models.BigIntegerField()
