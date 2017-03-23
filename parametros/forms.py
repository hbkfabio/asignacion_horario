from django import forms
from django.db.models import Q
from .sectioned_form import SectionedForm
from .models import (
    Carrera,
    Departamento,
    Plan,
    Modulo,
    Anio,
    Periodo,
    Bloque,
    Profesor,
    Semestre,
    Actividad,
)


import inspect


def retrieve_name(var):
    """
    Gets the name of var. Does it from the out most frame inner-wards.
    :param var: variable to get name from.
    :return: string
    """

    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]

def valida_campo(modelo, campo, valor):
    varname_campo = retrieve_name(campo)
    n = self.cleaned_data.get(varname_campo)
    query = modelo.objects.all().filter(campo = n)
    if query.exists():
        raise forms.ValidationError("%s ya se ha ingresado"%n)
        return False
    else:
        return n


def cleaned_nombre(self, modelo):
    """
    Función que valida para todos los formularios el campo nombre.

    Devuelve limpio de caracteres "especiales" los datos insertos en los
    diccionario de los formularios.

    This method returns the clean data, which is then inserted into the
    cleaned_data dictionary of the form.

    Valida si el valor del campo nombre existe en la base de datos.

    Validate if row value nombre exists in data base.

    param self: object value from form class
    param modelo: model object from model class
    return: string with data cleaned or raise message error
    """

    n = self.cleaned_data.get("nombre")
    pk = self.instance.pk
    query = modelo.objects.all().filter(nombre = n)
    query = query.filter(~Q(id=pk))
    if query.exists():
        raise forms.ValidationError("%s ya se ha ingresado"%n)
    return n


class MaestroForm(forms.ModelForm):

    class Meta:
        model = None
        fields = ["nombre", "descripcion"]


class DepartamentoForm(MaestroForm):

    MaestroForm.Meta.model = Departamento


    def clean_nombre(self):
        n = cleaned_nombre(self, Departamento)

        return n


class CarreraForm(MaestroForm):

    MaestroForm.Meta.model = Carrera

    def clean_nombre(self):
        n = cleaned_nombre(self, Carrera)

        return n


class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = ["nombre", "carrera"]


    def clean_carrera(self):
        c = self.cleaned_data.get("carrera")
        n = self.cleaned_data.get("nombre")
        pk = self.instance.pk
        query = Plan.objects.all().filter(carrera = c)
        query = query.filter(nombre = n)
        query = query.filter(~Q(id = pk))

        if query.exists():
            raise forms.ValidationError(
                "El plan %s ya fue ingresado para la carrera %s"%(n,c)
                )
        return c



class ModuloForm(forms.ModelForm):

    # query = Carrera.objects.all()
    # empty_label = "Seleccione una carrera"
    # carrera = forms.ModelChoiceField(queryset = query,
    #                     empty_label = empty_label,
    #                 )

    class Meta:
        model = Modulo

        fields = ["carrera",
                    "plan",
                    "nombre",
                    "semestre",
                    "horas_clase",
                    "horas_seminario",
                    "horas_laboratorio",
                    "horas_taller",
                    "horas_ayudantia",
                 ]


    def clean_plan(self):
        n = self.cleaned_data.get("nombre")
        s = self.cleaned_data.get("semestre")
        p = self.cleaned_data.get("plan")
        pk = self.instance.pk
        query = Modulo.objects.all().filter(plan = p)
        query = query.filter(semestre = s)
        query = query.filter(nombre = n)
        query = query.filter(~Q(id=pk))
        if query.exists():
            raise forms.ValidationError(
                "%s ya se ha ingresado para el %s modulo del plan %s"%(n,s,p)
                )
        return p


class AnioForm(forms.ModelForm):

    class Meta:
        model = Anio
        fields = ["nombre"]


    def clean_nombre(self):
        n = cleaned_nombre(self, Anio)
        return n


class PeriodoForm(forms.ModelForm):

    class Meta:
        model = Periodo
        fields = ["nombre", "anio"]


    def clean_anio(self):
        n = self.cleaned_data.get("nombre")
        a = self.cleaned_data.get("anio")
        pk = self.instance.pk
        query = Periodo.objects.all().filter(anio = a)
        query = query.filter(nombre = n)
        query = query.filter(~Q(id=pk))
        if query.exists():
            raise forms.ValidationError(
                "%s ya se ha ingresado para el año %s "%(n, a)
                )
        return a


class BloqueForm(forms.ModelForm):

    class Meta:
        model = Bloque
        fields = ["nombre"]


    def clean_nombre(self):
        n = cleaned_nombre(self, Bloque)

        return n



class ProfesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = ["nombre", "rut", "correo", "departamento"]


    def clean_nombre(self):
        n = cleaned_nombre(self, Profesor)

        return n

    def clean_correo(self):
        n = self.cleaned_data.get("correo")

        return n



class SemestreForm(forms.ModelForm):

    class Meta:
        model = Semestre
        fields = ["nombre"]

    def clean_nombre(self):
        n = cleaned_nombre(self, Semestre)

        return n


class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ["nombre",
                "identificador",]

    def clean_nombre(self):
        n = cleaned_nombre(self, Actividad)

        return n
