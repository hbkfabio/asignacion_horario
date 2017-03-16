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

    class Meta:
        ordering = ["-id"]


    def __str__(self):
        return "%s" %(self.nombre)


class Semestre(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Modulo(models.Model):
    nombre = models.CharField(u'Modulo', max_length=100)
    semestre = models.ForeignKey(Semestre, default=0)
    plan = models.ForeignKey(Plan)
    creditos = models.IntegerField(u'Créditos', default=0)
    horas_clase = models.IntegerField(u'Horas de clase', default=0)
    horas_seminario = models.IntegerField(u'Horas de seminario',default=0)
    horas_laboratorio = models.IntegerField(u'horas de laboratorio', default=0)
    horas_taller = models.IntegerField(u'Horas de Taller', default=0)
    horas_ayudantia = models.IntegerField(u'Horas de Ayudantía', default=0)

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
    rut = models.CharField(u'RUT', max_length=12, default='')
    correo = models.EmailField('Correo Electrónico', max_length=100, default='')

    def __str__(self):
        return self.nombre


class Anio(models.Model):
    nombre = models.CharField(max_length=4)

    class Meta:
        ordering = ["-nombre"]

    def __str__(self):
        return self.nombre


class Periodo(models.Model):
    nombre = models.CharField(max_length=50)
    anio = models.ForeignKey(Anio, null=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "%s del año %s"%(self.nombre,
                                self.anio.nombre)


class Bloque(models.Model):
    nombre = models.CharField(max_length=2)

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    identificador = models.CharField(max_length=1,
                    help_text="<sup>Escriba una letra para identifique la actividad</sup>",
                    default = "",
                    unique = True,
                    )

    def __str__(self):
        return self.nombre
