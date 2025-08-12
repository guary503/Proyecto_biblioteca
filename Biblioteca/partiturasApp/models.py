from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator #Estas clases son para validar un rango en algun IntegerField u otro.
# Create your models here.





class Compositor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    pais = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Instrumento(models.Model):
    nombre = models.CharField(max_length=50)
    familia = models.CharField(max_length=50)
    models.IntegerField(max_length=5)
    
    def __str__(self):
        return f'{self.nombre}'
    
    
class Partitura(models.Model):
    nombre = models.CharField(max_length=200)
    compositor = models.ForeignKey(Compositor, on_delete=models.CASCADE, related_name='partituras')
    genero = models.CharField(max_length=50, null=True, blank=True)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.PROTECT, related_name='instrumentos')
    fecha_creacion_partitura = models.DateField(null=True, blank=True)
    editorial = models.CharField(max_length=100 , null=True, blank=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    numero_opus = models.CharField(max_length=50, null=True, blank=True)
    
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} - {self.genero}'
    

"RETO DE GEMINI DE ALL DIAS HASTA EL 6"
#Dia 3 - reto - Crear el modelo
class Genero(models.Model):
    nombre = models.CharField(max_length=50,null=True,blank=True, unique=True)
    descripcion = models.TextField(null=True,blank=True)
    epoca_principal = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre}'
# Dia 4 - reto - administracion en admin.py
    

    def algo(self):
        pass






class PRUEBA(models.Model):   #modelo de prueba para crear un template
    titulo = models.CharField(max_length=50)
    compositor = models.ForeignKey(Compositor, related_name='compositor', null=True, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]  #se declara validators como atributo y espera una lista de los validadores.
        )