from django import forms
from .models import (PeriodoProfesorModulo,
                     ReservaBloqueProtegido,
                     CursosGrupo,
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


class CursosGrupoForm(forms.ModelForm):

    class Meta:
        model = CursosGrupo
        fields = [#"periodoprofesormodulo",
                    "modulo",
                ]
