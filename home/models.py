from django.db import models

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=10,null=True)
    description=models.CharField(max_length=50,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=7,null=True)
    image=models.ImageField(null=True,blank=True)

