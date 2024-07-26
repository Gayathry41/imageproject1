from django.db import models

# Create your models here.
class register(models.Model):
    productname=models.CharField(max_length=200,null=True)
    Quantity=models.IntegerField(null=True)
    Price=models.IntegerField(null=True)
    image=models.ImageField(upload_to="image/",null=True)