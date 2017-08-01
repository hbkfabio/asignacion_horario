#!/usr/bin/python3
from django.http import JsonResponse
from django.db.models import Q

from .models import (PeriodoProfesorModulo,
                     Horario,
                     Actividad,
                     HorarioTemp,
                     )

from parametros.models import(Modulo,
                              Profesor,
                              )
from collections import Counter

from .errores import *

import json


# def valida_choque_horario(dia_semana, bloque, periodo, semestre, valor):
#      pass

#     if valor == "":
#         return True, ""

#     horario = Horario.objects.all()
#     horario = horario.filter(dia_semana = dia_semana)
#     print (horario)
#     horario = horario.filter(periodoprofesormodulo__periodo=periodo)
#     print (horario)
#     horario = horario.filter(periodoprofesormodulo__modulo__semestre__nombre = semestre)
#     print (horario)


#     if bloque == "1":
#         horario = horario.filter(~Q(bloque1 = ""))
#     elif bloque == "2":
#         horario = horario.filter(~Q(bloque2 = ""))
#     elif bloque == "3":
#         horario = horario.filter(~Q(bloque3 = ""))
#     elif bloque == "4":
#         horario = horario.filter(~Q(bloque4 = ""))
#     elif bloque == "5":
#         horario = horario.filter(~Q(bloque5 = ""))
#     elif bloque == "6":
#         horario = horario.filter(~Q(bloque6 = ""))
#     elif bloque == "7":
#         horario = horario.filter(~Q(bloque7 = ""))
#     elif bloque == "8":
#         horario = horario.filter(~Q(bloque8 = ""))
#     elif bloque == "9":
#         horario = horario.filter(~Q(bloque9 = ""))
#     elif bloque == "10":
#         horario = horario.filter(~Q(bloque10 = ""))


#     if len(horario) == 0:
#         return True, ""
#     else:
#         msj = choque_horario()
#         return False, msj


def valida_choque_horario_profesor(periodo,
                                    modulo,
                                    profesor,
                                    dia,
                                    bloque,
                                    carrera):
    """
    Comprueba si existe choque de horarios por un profesor y modulo del mismo
    semestre para un bloque y día específico en estado reservado True.

    Recibe como parámetros:
        * periodo: id de la clase Periodo.
        * modulo: id de la clase Módulo.
        * profesor: id de la clase Profesor.
        * dia: numero del día de la semana, comenzando con 1 para lunes.
        * bloque: atributo nombre de la clase Bloque, extraido de la cabecera de
        la tabla de asignacion de horario.
        * carrera: id de la clase carrera.

    Retorna:
        Bool:
            * True, que no existe registro de choque_horario (Horario)
            * False, cuando existe un registro choque_horario (Horario)
        msj: para indicar el error del mensaje en formato JSON

    Para un profesor no se le puede agendar dos bloques de distintos módulos
    """

    h = Horario.objects.all()
    h = h.filter(dia_semana = dia,
                 bloque__nombre = bloque,
                 periodoprofesormodulo__periodo__id = periodo,
                 reservado = True,
                 periodoprofesormodulo__profesor__id=profesor
                 )

    h = h.exclude(periodoprofesormodulo__modulo__id = modulo)
    msj = ""

    if h.exists():
        p = Profesor.objects.all().filter(id = profesor)
        m = Modulo.objects.all().filter(id=h[0].periodoprofesormodulo.modulo.id)
        msj = "El Profesor %s "%p[0].nombre
        msj += "ya tiene este bloque reservado con el módulo de %s"%m[0].nombre
        msj = {"sucess": False, "msj": msj}
        msj = json.dumps(msj).encode('utf_8')

        return False, msj

    else:
        return True, msj


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

        msj = {"sucess": False, "msj": msj}
        msj = json.dumps(msj).encode('utf_8')

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


def valida_choque_horario_modulo_semestre(bloque, dia, plan):
    """
    Método que permite establecer que no pueda existir un choque de horario
    con módulo del mismo nivel en un semestre determinado.
    Recibe:
        * bloque: Objecto Bloque
        * dia: numero del día de la semana, comenzando con 1 para lunes.
        * plan: id de la clase Plan.
    Retorna dos elementos:
        bool:
            True: Cuando puede agregar actividad al Horario
            False: No puede agregar una actividad al Horario
        string:
            msj: cuando existe un error en la validación
    """

    h = Horario.objects.all()
    h = h.filter(bloque=bloque,
                dia_semana = dia,
                periodoprofesormodulo__modulo__plan__id=plan
                )

    msj = ""


    if h.exists():
        plan = h[0].periodoprofesormodulo.modulo.plan.nombre
        modulo = h[0].periodoprofesormodulo.modulo.nombre
        nivel = h[0].periodoprofesormodulo.modulo.semestre.nombre


        msj = "El bloque seleccionado no se puede agendar: \n"
        msj += "El módulo %(modulo)s del %(plan)s, "%{"modulo": modulo,
                                                    "plan": plan,
                                                    }
        msj += "%(nivel)s semestre ya lo tiene reservado"%{"nivel":nivel}

        msj = {"sucess": False, "msj": msj}
        msj = json.dumps(msj).encode('utf_8')
        return False, msj

    return True, msj

# def valida_ppm_horario(actividad, horario, ppm, modulo_id, nuevo):
    """
    Método utilizado para inicializar una serie de validaciones al momento de
    agendar un horario para un profesor, modulo, periodo determinado.

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


#    v, msj = valida_cantidad_horas(actividad, horario, modulo_id, nuevo)
    # v, msj = chequea_choque_horario_profesor(horario)

    # return v, msj
    # if not v:
    #     return v, msj


