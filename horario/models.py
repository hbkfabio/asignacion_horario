from django.db import models
from parametros.models import (Periodo,
                             Profesor,
                             Modulo,
                             Bloque
                              )
# Create your models here.

class PeriodoProfesorModulo(models.Model):
    periodo = models.ForeignKey(Periodo)
    profesor = models.ForeignKey(Profesor)
    modulo = models.ForeignKey(Modulo)

    def __str__(self):
        return ('%s %s %s')%(self.periodo, self.profesor, self.modulo)


# class Horario(models.Model):
#     periodoprofesormodulo = models.ForeignKey(PeriodoProfesorModulo)
#     bloque1 = models.CharField(max_length=1)
#     bloque2 = models.CharField(max_length=1)
#     bloque3 = models.CharField(max_length=1)
#     bloque4 = models.CharField(max_length=1)
#     bloque5 = models.CharField(max_length=1)
#     bloque6 = models.CharField(max_length=1)
#     bloque7 = models.CharField(max_length=1)
#     bloque8 = models.CharField(max_length=1)
#     bloque9 = models.CharField(max_length=1)
#     bloque10 = models.CharField(max_length=1)
#     dia_semana = models.CharField(max_length=20, default="")



class Horario(models.Model):
    periodoprofesormodulo = models.ForeignKey(PeriodoProfesorModulo)
    bloque = models.ForeignKey(Bloque)
    dia_semana = models.CharField(max_length=20, default="")



class ReservaBloqueProtegido(models.Model):
    bloque1 = models.BooleanField()
    bloque2 = models.BooleanField()
    bloque3 = models.BooleanField()
    bloque4 = models.BooleanField()
    bloque5 = models.BooleanField()
    bloque6 = models.BooleanField()
    bloque7 = models.BooleanField()
    bloque8 = models.BooleanField()
    bloque9 = models.BooleanField()
    bloque10 = models.BooleanField()
    dia_semana = models.CharField(max_length=20, default="")
