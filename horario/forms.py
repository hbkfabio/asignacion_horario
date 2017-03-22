from django import forms
from .models import (PeriodoProfesorModulo,
                     ReservaBloqueProtegido,
                     )
from parametros.models import (Carrera,
                               Plan,
                               )

class PeriodoProfesorModuloForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PeriodoProfesorModuloForm, self).__init__(*args, **kwargs)
        self.fields['carrera'].widget= forms.Select(attrs={'class':'get_carrera'})
        self.fields['carrera'].empty_label="Seleccione una carrera"
        self.fields['carrera'].queryset = Carrera.objects.all()

        self.fields['plan'].widget= forms.Select(attrs={'class':'get_plan'})
        self.fields['periodo'].widget= forms.Select(attrs={'class':'get_periodo'})
        self.fields['profesor'].widget= forms.Select(attrs={'class':'get_profesor'})
        self.fields['modulo'].widget= forms.Select(attrs={'class':'get_modulo'})


    class Meta:
        model = PeriodoProfesorModulo
        fields = ["carrera",
                "plan",
                "periodo",
                "profesor",
                "modulo"
                ]


class ReservaBloqueProtegidoForm(forms.ModelForm):

    class Meta:
        model = ReservaBloqueProtegido
        fields = ["bloque1", "bloque2", "bloque3",
                "bloque4", "bloque5", "bloque6",
                "bloque7", "bloque8", "bloque9",
                "bloque10",
                ]
