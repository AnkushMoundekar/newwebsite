from django.db import models

# Create your models here.

class Products(models.Model):
    name:models.CharField(max_length=30)
    descciption:models.CharField(max_length=200)
    image:models.ImageField
