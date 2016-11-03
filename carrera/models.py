from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField (max_length=200, blank=True, null=True)



class Plan(models.Model):
    nombre = models.CharField(max_length=10)


class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    plan = models.ForeignKey(Plan)


class Profesor(models.Model):
    nombre = models.CharField
