from django.db import models
from django.conf import settings 
from django.db import models 
from django.utils import timezone 

# Create your models here.

class Coche(models.Model):
    # matricula = models.CharField(max_length=10, primary_key=True, default='ABC1234', unique=True)
    marca = models.CharField(max_length=100)
    ruedas = models.IntegerField()
    cilindrada = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.marca
    
class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    localidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre