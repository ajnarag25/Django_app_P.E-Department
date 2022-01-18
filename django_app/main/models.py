from django.db import models

# Create your models here.
# class Registration(models.Model):
#     firstname = models.CharField(max_length=200)
#     lastname = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     gender = models.CharField(max_length=100)
#     email = models.EmailField(max_length=200)
#     course = models.CharField(max_length=100)

class Buy(models.Model):
    idnum = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    gender = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    shirt = models.IntegerField()
    short = models.IntegerField()
    slacks = models.IntegerField()
    joggingpant = models.IntegerField()
    size = models.CharField(max_length=100)

class Reserve(models.Model):
    idnum = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    gender = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    shirt = models.IntegerField()
    short = models.IntegerField()
    slacks = models.IntegerField()
    joggingpant = models.IntegerField()
    size = models.CharField(max_length=100)

class Borrow(models.Model):
    idnum = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    course = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    items = models.CharField(max_length=100)
    quantity = models.IntegerField()
    dateofborrow = models.DateField()
    dateofreturn = models.DateField()





