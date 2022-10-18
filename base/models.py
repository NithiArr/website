from django.db import models

class crudst(models.Model):
    fromdes = models.CharField(max_length = 100)
    todes = models.CharField(max_length = 100)
    status = models.CharField(max_length= 100)# Create your models here.
    sno = models.IntegerField()
    price = models.IntegerField(null=True)