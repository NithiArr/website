from random import choices
from secrets import choice
from django.db import models

class crudst(models.Model):
    STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
    fromdes = models.CharField(max_length = 100)
    todes = models.CharField(max_length = 100)
    status = models.CharField(max_length= 100,null=True, choices=STATUS)# Create your models here.
    sno = models.IntegerField()
    price = models.IntegerField(null=True)