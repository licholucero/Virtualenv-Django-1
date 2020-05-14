from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.AutoField(primary_key=True)
    def __str__(self):
        return '{}'.format(self.nombre)

class Libro(models.Model):
    codigo = models.AutoField(primary_key =True)
    codigo_autor = models.ForeignKey(Autor, on_delete=models.CASCADE) 
    titulo = models.CharField(max_length=20)
    editorial = models.CharField(max_length=20)
    paginas = models.IntegerField()
    def __str__(self):
        return '{} {}'.format(self.titulo,self.editorial)

class Ejemplar (models.Model):
    codigo = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE) 
    localizacion =models.CharField(max_length=30)
    def __str__(self):
        return '{}'.format(self.localizacion)

class Usuario(models.Model):
    codigo = models.AutoField(primary_key =True)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    ejemplares = models.ManyToManyField(Ejemplar)
    def __str__(self):
        return '{} {} {}'.format(self.nombre,self.direccion,self.telefono)


