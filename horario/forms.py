from django import forms
from .models import (PeriodoProfesorModulo,
                     )

class PeriodoProfesorModuloForm(forms.ModelForm):

    class Meta:
        model = PeriodoProfesorModulo
        fields = ["periodo", "profesor", "modulo"]
