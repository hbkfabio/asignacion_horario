from django.shortcuts import render, redirect
from django.contrib import messages
from parametros.views import (ViewListView,
                            ViewCreateView,
                            ViewUpdateView,
                            ViewDeleteView,
                            )

from .models import (PeriodoProfesorModulo,
                     )

from parametros.models import (Periodo,
                               )

from .forms import (PeriodoProfesorModuloForm,
                    )

from django.views.generic.base import TemplateView

from django.views.decorators.csrf import csrf_exempt
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
    success_message = "El Profesor %(nombre)s ha sido actualizado"
    success_url = "/periodoprofesormodulo/"


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


#@csrf_exempt
class HorarioTemplateView(TemplateView):

    template_name = "horario/base_horario.html"

    def get_context_data(self, **kwargs):

        periodo = self.request.GET.get("periodo")
        context = super(HorarioTemplateView, self).get_context_data(**kwargs)
        context["titulo"] = "Horario"
        context["dia_semana"] = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes')
        queryset = PeriodoProfesorModulo.objects.all()
        if periodo is not None or periodo !="0":
            context["queryset_profesor_modulo"] = queryset.filter(periodo=periodo)
        context["queryset_periodo"] = Periodo.objects.all().order_by('-id')
        return context


def HorarioView(request):

    titulo = "Horario"
    dia_semana = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes')

    print (request.GET.get("periodo"))
    queryset = PeriodoProfesorModulo.objects.all()
    # if request.GET.get("periodo") is not None:
    #     queryset = queryset.filter(periodo=request.GET.get("periodo"))


    # try:
    #     if not request.POST["periodo"]:
    #         queryset = PeriodoProfesorModulo.objects.all()
    # except:
        #queryset = PeriodoProfesorModulo.objects.all().filter(periodo=request.POST["periodo"])
    #     pass

    # queryset = PeriodoProfesorModulo.objects.all()
    queryset_periodo = Periodo.objects.all().order_by('-id')
    context = {

        "titulo":titulo,
        "dia_semana":dia_semana,
        "queryset" : queryset,
        "queryset_periodo": queryset_periodo,

    }


    return render(request, "horario/base_horario.html", context)
