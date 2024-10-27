from django.db import models

# Create your models here.
class Fyv(models.Model):
    codigo=models.CharField(primary_key=True,max_length=7)
    nombre=models.CharField(max_length=50, null=False)
    temporada= models.CharField(max_length=20, null=False)
    calorias=models.IntegerField(null=False)
    vitaminas=models.CharField(max_length=20)
    precio=models.IntegerField(null=False)
    stack=models.IntegerField(null=False)
    
    def __str__(self) -> str:
        return self.nombre