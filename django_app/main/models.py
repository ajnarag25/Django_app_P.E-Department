from django.db import models

# Create your models here.
class Registration(models.Model):
    firstname= models.CharField(max_length=200)
    lastname= models.CharField(max_length=200)
    username= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
