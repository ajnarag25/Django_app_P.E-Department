from django.db import models

# Create your models here.
class Registration(models.Model):
    firstname= models.CharField(max_length=200)
    lastname= models.CharField(max_length=200)
    username= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    gender= models.CharField(max_length=100)
    email= models.EmailField(max_length=200)
    course= models.CharField(max_length=100)
