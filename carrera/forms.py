from django import forms
from .models import *

class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = ["nombre", "descripcion"]
