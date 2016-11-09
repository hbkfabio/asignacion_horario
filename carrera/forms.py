from django import forms
from .models import (
    Carrera,
    Departamento,
    Plan,
    Modulo,
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
        fields = ["nombre", "plan"]

# class DepartamentoForm(forms.ModelForm):

#     class Meta:
#         model = Departamento
#         fields = ["nombre", "descripcion"]




# class CarreraForm(forms.ModelForm):

#     class Meta:
#         model = Carrera
#         fields =



