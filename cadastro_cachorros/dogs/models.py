from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=100)

class Dog(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
