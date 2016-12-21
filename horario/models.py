from django.db import models
from parametros.models import Periodo, Profesor, Modulo
# Create your models here.

class PeriodoProfesorModulo(models.Model):
    periodo = models.ForeignKey(Periodo)
    profesor = models.ForeignKey(Profesor)
    modulo = models.ForeignKey(Modulo)

    def __str__(self):
        return ('%s %s %s')%(self.periodo, self.profesor, self.modulo)
