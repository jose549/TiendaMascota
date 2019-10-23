from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='fotos/')
    
    def __str__(self):
        return str(self.id) + ", " + self.nombre + ", " + str(self.precio) + ", " + str(self.stock) + ", " + str(self.foto)
