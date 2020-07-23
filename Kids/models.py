from django.db import models
# Create your models here.

class Fashionkids(models.Model):
    price=models.IntegerField()
    img=models.ImageField(upload_to='Pics')