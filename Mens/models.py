from django.db import models

# Create your models here.

class Fashionmen(models.Model):
    price=models.IntegerField()
    img=models.ImageField(upload_to='Pics')