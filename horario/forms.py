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
        fields = ["periodo",
                "carrera",
                "plan",
                "modulo",
                "profesor",
                ]


class ReservaBloqueProtegidoForm(forms.ModelForm):

    class Meta:
        model = ReservaBloqueProtegido
        fields = ["bloque",
                    "reservado",
                ]
