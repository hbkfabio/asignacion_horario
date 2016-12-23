from django.db import models
from parametros.models import Periodo, Profesor, Modulo
# Create your models here.

class PeriodoProfesorModulo(models.Model):
    periodo = models.ForeignKey(Periodo)
    profesor = models.ForeignKey(Profesor)
    modulo = models.ForeignKey(Modulo)

    def __str__(self):
        return ('%s %s %s')%(self.periodo, self.profesor, self.modulo)


class horario(models.Model):
    periodoprofesormodulo = models.ForeignKey(PeriodoProfesorModulo)
    bloque1 = models.CharField(max_length=1)
    bloque2 = models.CharField(max_length=1)
    bloque3 = models.CharField(max_length=1)
    bloque4 = models.CharField(max_length=1)
    bloque5 = models.CharField(max_length=1)
    bloque6 = models.CharField(max_length=1)
    bloque7 = models.CharField(max_length=1)
    bloque8 = models.CharField(max_length=1)
    bloque9 = models.CharField(max_length=1)
    bloque10 = models.CharField(max_length=1)


    
