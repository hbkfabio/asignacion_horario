from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField (max_length=200, blank=True, null=True)


class Plan(models.Model):
    nombre = models.CharField(max_length=10)
    carrera = models.Foreignkey(Carrera)


class Modulo(models.Model):
    nombre = models.CharField(max_length=50)
    plan = models.ForeignKey(Plan)


class Departamento(models.Model):
    nombre = models.CharField(max_length=50)


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento)


class Anio(models.Model):
    nombre = models.CharField(max_length=4)


class Periodo(models.Model):
    nombre = models.CharField(max_length=10)
    anio = models.ForeignKey(Anio)

class Bloque(models.Model):
    nombre = models.CharField(max_length=2)
