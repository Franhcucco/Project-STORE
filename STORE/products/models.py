from django.db import models

# Create your models here.
class shoes(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    size = models.IntegerField()
    stock = models.BooleanField(default=True)
    pesos = '$'

    def __str__(self):
        return self.name

class tShirt(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    size = models.CharField(max_length=3)
    stock = models.BooleanField(default=True)
    pesos = '$'

    def __str__(self):
        return self.name

class pants(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    size = models.IntegerField()
    stock = models.BooleanField(default=True)
    pesos = '$'

    def __str__(self):
        return self.name


