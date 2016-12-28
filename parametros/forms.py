from django import forms
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
)



class MaestroForm(forms.ModelForm):

    class Meta:
        model = None
        fields = ["nombre", "descripcion"]


class DepartamentoForm(MaestroForm):

     MaestroForm.Meta.model = Departamento


class CarreraForm(MaestroForm):

    MaestroForm.Meta.model = Carrera


class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = ["nombre", "carrera"]


class ModuloForm(forms.ModelForm):

    class Meta:
        model = Modulo

        fields = ["nombre",
                    "semestre",
                    "plan",
                    "horas_clase",
                    "horas_seminario",
                    "horas_laboratorio",
                    "horas_taller",
                    "horas_ayudantia",
                 ]


class AnioForm(forms.ModelForm):

    class Meta:
        model = Anio
        fields = ["nombre"]


class PeriodoForm(forms.ModelForm):

    class Meta:
        model = Periodo
        fields = ["nombre", "anio"]


class BloqueForm(forms.ModelForm):

    class Meta:
        model = Bloque
        fields = ["nombre"]


class ProfesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = ["nombre", "rut", "correo", "departamento"]



class SemestreForm(forms.ModelForm):

    class Meta:
        model = Semestre
        fields = ["nombre"]
