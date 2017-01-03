
def exceso_horas(query, valor):
    msj = ""
    query = query.periodoprofesormodulo
    modulo = query.modulo.nombre
    profesor = query.profesor.nombre
    plan = query.modulo.plan.nombre

    if (valor == "C"):
        horas = query.modulo.horas_clase
        valor = "Clases"

    elif (valor == "A"):
        horas = query.modulo.horas_ayudantia
        valor = "Ayudantía"

    elif (valor == "L"):
        horas = query.modulo.horas_laboratorio
        valor = "Laboratorio"

    elif (valor == "S"):
        horas = query.modulo.horas_seminario
        valor = "Seminario"

    elif(valor == "T"):
         horas = query.modulo.horas_taller
         valor = "Taller"

    msj = """El Modulo %s para el profesor %s plan %s ya tiene
                los %s bloques asignados para %s""" %(
            modulo,
            profesor,
            plan,
            horas,
            valor
            )
    return msj
