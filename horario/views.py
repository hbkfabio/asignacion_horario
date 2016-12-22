from django.shortcuts import render
from django.contrib import messages
from parametros.views import (ViewListView,
                            ViewCreateView,
                            ViewUpdateView,
                            ViewDeleteView,
                            )

from .models import (PeriodoProfesorModulo,
                     )

from .forms import (PeriodoProfesorModuloForm,
                    )
# Create your views here.


class PeriodoProfesorModuloListView(ViewListView):
    model = PeriodoProfesorModulo
    template_name = "horario/base_horario.html"
    titulo = "Asignación Profesor Módulo"
    extra_context = {}


class PeriodoProfesorModuloCreateView(ViewCreateView):
    form_class = PeriodoProfesorModuloForm
    template_name = "horario/form.html"
    titulo = "Agrega Asignacion de periodo-profesor-modulo"
    success_message = "La Asignacion %(nombre)s ha sido creado"
    success_url = "/periodoprofesormodulo/"


    def get_success_message(self, cleaned_data):
    #cleaned_data is the cleaned data from the form which is used for string formatting
        return self.success_message % dict(cleaned_data,
                                       nombre=self.object.profesor.nombre)


class PeriodoProfesorModuloUpdateView(ViewUpdateView):
    model = PeriodoProfesorModulo
    form_class = PeriodoProfesorModuloForm
    template_name = "horario/form.html"
    success_message = "El Profesor %(name)s ha sido actualizado"
    success_url = "/plan/"


    def get_success_message(self, cleaned_data):
    #cleaned_data is the cleaned data from the form which is used for string formatting
        return self.success_message % dict(cleaned_data,
                                       nombre=self.object.profesor.nombre)



class PeriodoProfesorModuloDeleteView(ViewDeleteView):
    model = PeriodoProfesorModulo
    template_name = "parametros/elimina.html"
    success_message = 'El Profesor %(nombre)s ha sido Eliminado'
    success_url = "/periodoprofesormodulo/"


    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message %dict(nombre=obj,))
        return super(ViewDeleteView, self).delete(request, *args, **kwargs)

