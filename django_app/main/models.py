from django.db import models

# Create your models here.
class Registration(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    course = models.CharField(max_length=100)
    def __str__(self):
        return self.firstname

class Buy(models.Model):
    idnum = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    shirt = models.CharField(max_length=100)
    short = models.CharField(max_length=100)
    slacks = models.CharField(max_length=100)
    joggingpant = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

class Reserve(models.Model):
    idnum = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    shirt = models.CharField(max_length=100)
    short = models.CharField(max_length=100)
    slacks = models.CharField(max_length=100)
    joggingpant = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

class Borrow(models.Model):
    idnum = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    items = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    dateofborrow = models.CharField(max_length=100)
    dateofreturn = models.CharField(max_length=100)





