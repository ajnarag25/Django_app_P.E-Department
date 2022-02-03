from ast import mod
from django.db import models

class Buy(models.Model):
    idnum = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
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
    contact = models.CharField(max_length=100)
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
    contact = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    items = models.CharField(max_length=100)
    quantity = models.IntegerField()
    dateofborrow = models.DateField()
    dateofreturn = models.DateField()


class Inventory(models.Model):
    equipment = models.CharField(max_length=100)
    quantity = models.IntegerField()
    borrowers = models.IntegerField()


