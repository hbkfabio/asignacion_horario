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


def valida_cantidad_horas(actividad, query, modulo_id, nuevo):
    """
    Metodo que valida la cantidad de horas definidas para una actividad
    versus las cantidades de horas que se procede a agendar

    Recibe los parametros:
        * actividad: Que es el atributo identificador de la Clase
        ActividadCreateView.
        * query: Trae el query (Horario u HorarioTemp).
        * temp: Utilizado para indicar si la Clase a Consultar es Horario (edita
        objeto) u HorarioTemp (nuevo objeto).
        * nuevo: Boolean que referencia si es un nuevo objeto PPM o si es una
        edición.

        Retorna:
            True: Cuando puede agregar actividad al Horario
            False: No puede agregar una actividad al Horario
    """

    a = query.filter(actividad=actividad)
    a = len(a)+1
    modulo = Modulo.objects.all().filter(id = modulo_id)

    if(actividad.identificador == 'C'):
        if (a>modulo[0].horas_clase):
            msj = "%(nombre)s ya tiene agendada los %(clases)s bloques"%{
                "nombre": modulo[0].nombre,
                "clases": modulo[0].horas_clase,
                }
            return False, msj
        else:
            return True, None


    # if valor == "":
    #     return True, ""
    # print (query)

    #query = query.order_by("dia_semana") #temporal

    # query_values = query.values("bloque1",
    #                     "bloque2",
    #                     "bloque3",
    #                     "bloque4",
    #                     "bloque5",
    #                     "bloque6",
    #                     "bloque7",
    #                     "bloque8",
    #                     "bloque9",
    #                     "bloque10",
    #                     )

    # cuenta=0
    # for i in query_values:
    #     t=Counter(i.values())
    #     print("t: ", t)
    #     cuenta+=t[valor]


    # if (valor == "C"):
    #     q = query[0].periodoprofesormodulo.modulo.horas_clase
    # elif (valor == "L"):
    #     q = query[0].periodoprofesormodulo.modulo.horas_laboratorio
    # elif(valor == "S"):
    #     q = query[0].periodoprofesormodulo.modulo.horas_seminario
    # elif(valor == "T"):
    #     q = query[0].periodoprofesormodulo.modulo.horas_taller
    # elif(valor == "A"):
    #     q = query[0].periodoprofesormodulo.modulo.horas_ayudantia

    # if q > cuenta:
    #     return True, " "
    # else:
    #     msj = exceso_horas(query[0], valor)
    #     return False, msj




    
