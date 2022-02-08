from ast import mod
from django.db import models

class Buy(models.Model):
    idnum = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
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
    mop = models.CharField(max_length=100)
    addresses = models.CharField(max_length=100)
    total = models.IntegerField()
    status = models.CharField(max_length=100)
    note = models.CharField(max_length=1000)

class Reserve(models.Model):
    idnum = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
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
    total = models.IntegerField()
    status = models.CharField(max_length=100)
    note = models.CharField(max_length=1000)

class Borrow(models.Model):
    idnum = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    items = models.CharField(max_length=100)
    quantity = models.IntegerField()
    dateofborrow = models.CharField(max_length=100)
    dateofreturn = models.CharField(max_length=100)
    timeofborrow = models.CharField(max_length=100)
    timeofreturn = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    note = models.CharField(max_length=1000)


class Inventory(models.Model):
    equipment = models.CharField(max_length=100)
    quantity = models.IntegerField()
    borrowers = models.IntegerField()


