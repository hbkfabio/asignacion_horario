
def exceso_horas(query, valor):
    msj = ""
    if (valor == "C"):
        query = query.periodoprofesormodulo
        modulo = query.modulo.nombre
        profesor = query.profesor.nombre
        plan = query.modulo.plan.nombre
        horas_clase = query.modulo.horas_clase
        msj = """El Modulo %s para el profesor %s plan %s ya tiene
                los %s bloques asignados para clases """ %(
            modulo,
            profesor,
            plan,
            horas_clase,
            )

    return msj
