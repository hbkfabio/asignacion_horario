from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField (max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Plan(models.Model):
    nombre = models.CharField(max_length=10)
    carrera = models.ForeignKey(Carrera, null=True)

    def __str__(self):
        return "%s de %s" %(self.nombre, self.carrera.nombre)

class Modulo(models.Model):
    nombre = models.CharField(max_length=50)
    plan = models.ForeignKey(Plan)
    credito = models.IntegerField(default=0)

    def __str__ (self):
        return ("%s del %s")%(self.nombre, self.plan.nombre)


class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(u'Descripción', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento)


class Anio(models.Model):
    nombre = models.CharField(max_length=4)

    def __str__(self):
        return self.nombre


class Periodo(models.Model):
    nombre = models.CharField(max_length=50)
    anio = models.ForeignKey(Anio, null=True)

    def __str__(self):

        return "%s del año %s"%(self.nombre,
                                self.anio.nombre)

class Bloque(models.Model):
    nombre = models.CharField(max_length=2)
