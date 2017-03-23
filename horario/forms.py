from django import forms
from .models import (PeriodoProfesorModulo,
                     ReservaBloqueProtegido,
                     )
from parametros.models import (Carrera,
                               Plan,
                               )

class PeriodoProfesorModuloForm(forms.ModelForm):

    class Meta:
        model = PeriodoProfesorModulo
        fields = ["carrera",
                "plan",
                "modulo",
                "periodo",
                "profesor",
                ]


class ReservaBloqueProtegidoForm(forms.ModelForm):

    class Meta:
        model = ReservaBloqueProtegido
        fields = ["bloque1", "bloque2", "bloque3",
                "bloque4", "bloque5", "bloque6",
                "bloque7", "bloque8", "bloque9",
                "bloque10",
                ]
