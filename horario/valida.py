#!/usr/bin/python3
from django.http import JsonResponse
from django.db.models import Q

from .models import (PeriodoProfesorModulo,
                     Horario,
                     Actividad,
                     HorarioTemp,
                     )

from parametros.models import(Modulo,
                              )
from collections import Counter

from .errores import *


def valida_choque_horario(dia_semana, bloque, periodo, semestre, valor):

    if valor == "":
        return True, ""

    horario = Horario.objects.all()
    horario = horario.filter(dia_semana = dia_semana)
    print (horario)
    horario = horario.filter(periodoprofesormodulo__periodo=periodo)
    print (horario)
    horario = horario.filter(periodoprofesormodulo__modulo__semestre__nombre = semestre)
    print (horario)


    if bloque == "1":
        horario = horario.filter(~Q(bloque1 = ""))
    elif bloque == "2":
        horario = horario.filter(~Q(bloque2 = ""))
    elif bloque == "3":
        horario = horario.filter(~Q(bloque3 = ""))
    elif bloque == "4":
        horario = horario.filter(~Q(bloque4 = ""))
    elif bloque == "5":
        horario = horario.filter(~Q(bloque5 = ""))
    elif bloque == "6":
        horario = horario.filter(~Q(bloque6 = ""))
    elif bloque == "7":
        horario = horario.filter(~Q(bloque7 = ""))
    elif bloque == "8":
        horario = horario.filter(~Q(bloque8 = ""))
    elif bloque == "9":
        horario = horario.filter(~Q(bloque9 = ""))
    elif bloque == "10":
        horario = horario.filter(~Q(bloque10 = ""))


    if len(horario) == 0:
        return True, ""
    else:
        msj = choque_horario()
        return False, msj


def cuenta_cantidad_horas(nombre, actividad, actual, total):
    """
    Método para contar la cantidad de horas asociadas a un módulo.
    Depende del método valida_cantidad_horas.

    Recibe tres parámetros:
        * nombre = nombre del módulo de la clase Modulo.
        * actual = es la cantidad de bloques agendados en clase Horario u
        HorarioTemp.
        * total = cantidad de horas total asociadas al módulo (clase Modulo).

    Retorna dos parámetros:
        * Bool,
            * True, cuando la actual < total
            * False, cuando actual > total
        * String,
            * msj, cuando actual > total, y el bool es False
    """

    if (actual>total):
        msj = "%(nombre)s ya tiene agendada los "%{"nombre": nombre}
        msj += "%(identificador)s bloques de "%{"identificador":total}
        msj += "%(actividad)s"%{"actividad":actividad.nombre}
        return False, msj
    else:
        return True, None

def valida_cantidad_horas(actividad, query, modulo_id, nuevo):
    """
    Metodo que valida la cantidad de horas definidas para una actividad
    versus las cantidades de horas que se procede a agendar

    Recibe los parametros:
        * actividad: Que es el atributo identificador de la Clase
        ActividadCreateView.
        * query: Trae el query (Horario u HorarioTemp).
        * modulo_id: Trae el id de la clase modulo.
        * temp: Utilizado para indicar si la Clase a Consultar es Horario (edita
        objeto) u HorarioTemp (nuevo objeto).
        * nuevo: Boolean que referencia si es un nuevo objeto PPM o si es una
        edición,True para Nuevo, False para editar.

        Retorna dos elementos:
            bool:
                True: Cuando puede agregar actividad al Horario
                False: No puede agregar una actividad al Horario
            string:
                msj: cuando existe un error en la validación
    """

    #Variables por defecto
    c = True
    msj = ""

    a = query.filter(actividad=actividad)
    a = len(a)+1
    modulo = Modulo.objects.all().filter(id = modulo_id)

    if actividad is None:
        return True, None

    if(actividad.identificador == 'C'):
        c, msj = cuenta_cantidad_horas(modulo[0].nombre,
                                       actividad,
                                        a,
                                modulo[0].horas_clase)
    elif(actividad.identificador == 'L'):
        c, msj = cuenta_cantidad_horas(modulo[0].nombre,
                                       actividad,
                                        a,
                                        modulo[0].horas_laboratorio)
    elif(actividad.identificador == 'S'):
        c, msj = cuenta_cantidad_horas(modulo[0].nombre,
                                        actividad,
                                        a,
                                        modulo[0].horas_seminario)
    elif(actividad.identificador == 'T'):
        c, msj = cuenta_cantidad_horas(modulo[0].nombre,
                                       actividad,
                                       a,
                                       modulo[0].horas_taller)
    elif(actividad.identificador == 'A'):
        c, msj = cuenta_cantidad_horas(modulo[0].nombre,
                                       actividad,
                                       a,
                                       modulo[0].horas_ayudantia)
    return c, msj


    
