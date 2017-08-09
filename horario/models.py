#!/usr/bin/python3
from django.db import models
from parametros.models import (Periodo,
                             Profesor,
                             Modulo,
                             Bloque,
                             Carrera,
                             Plan,
                             Actividad,
                              )
# Create your models here.

class PeriodoProfesorModulo(models.Model):
    carrera = models.ForeignKey(Carrera, default=None)
    plan = models.ForeignKey(Plan, default=None)
    periodo = models.ForeignKey(Periodo, default=None)
    modulo = models.ForeignKey(Modulo, default=None)
    profesor = models.ForeignKey(Profesor, default=None)
    compartido = models.BooleanField(u'Cursos Grupos', default=False,
        help_text="<small>Check si el módulo será un curso compartido</small>",
        );

    def __str__(self):
        return ('%s %s %s')%(self.periodo, self.profesor, self.modulo)


class Horario(models.Model):
    periodoprofesormodulo = models.ForeignKey(PeriodoProfesorModulo)
    dia_semana = models.CharField(max_length=20, default="")
    reservado = models.BooleanField(default=False)
    bloque = models.ForeignKey(Bloque, default=None)
    actividad= models.ForeignKey(Actividad, default=None, null=True, blank=True)


class ReservaBloqueProtegido(models.Model):
    bloque = models.ForeignKey(Bloque, default=None)
    reservado = models.BooleanField(default=False)

    class Meta:
        ordering = ["bloque"]

class CursosGrupo(models.Model):
    periodoprofesormodulo = models.ForeignKey(PeriodoProfesorModulo, default=None)
    modulo = models.ForeignKey(Modulo, default=None)

    def __str__(self):
        return self.modulo


class HorarioTemp(models.Model):
    """
    Clase utilitaria para almacenar atributos temporales que pudiesen
    servir para implementar clases que dependen de acciones posteriores
    a fin de efectuarse de buena manera
    Clase pivot
    """
    dia_semana = models.CharField(max_length=20, default="", null=True)
    reservado = models.BooleanField(default=False)
    bloque = models.ForeignKey(Bloque, default=None, null=True)
    actividad= models.ForeignKey(Actividad, default=None, null=True)
    carrera = models.ForeignKey(Carrera, default=None, null=True)
    modulo = models.ForeignKey(Modulo, default=None, null=True)
    profesor = models.ForeignKey(Profesor, default=None, null=True)


