from django.db import models

# Create your models here.

class Enterhome(models.Model):
    name= models.CharField(max_length=100)
    desc= models.TextField()
    img= models.ImageField(upload_to='homepics')
    location=models.CharField(max_length=100)
    price=models.IntegerField()
    offer=models.BooleanField(default=False)