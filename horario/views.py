from django.shortcuts import render, redirect
from django.contrib import messages
from parametros.views import (ViewListView,
                            ViewCreateView,
                            ViewUpdateView,
                            ViewDeleteView,
                            )

from .models import (PeriodoProfesorModulo,
                     Horario,
                     )

from parametros.models import (Periodo,
                               )

from .forms import (PeriodoProfesorModuloForm,
                    )

from django.views.generic.base import TemplateView

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import simplejson as json
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


@csrf_exempt
def HorarioSave(request):

    if request.method == "POST" and request.is_ajax():
        model = Horario
        dic = request.POST.get("diccionario")
        dic = json.loads(dic)
        print (dic)

        bloque1 = dic["accion bloque1"]
        bloque2 = dic["accion bloque2"]
        bloque3 = dic["accion bloque3"]
        bloque4 = dic["accion bloque4"]
        bloque5 = dic["accion bloque5"]
        bloque6 = dic["accion bloque6"]
        bloque7 = dic["accion bloque7"]
        bloque8 = dic["accion bloque8"]
        bloque9 = dic["accion bloque9"]
        bloque10 = dic["accion bloque10"]

        profesor = dic["profesor"];
        modulo = dic["modulo"]
        plan = dic["plan"]
        dia_semana = dic["dia_semana"]

        query_ppm = PeriodoProfesorModulo.objects.all().filter(
                        profesor__nombre=profesor,
                        modulo__nombre=modulo,
                        modulo__plan__nombre = plan,
        )

        query_horario = Horario.objects.all()
        query_horario = query_horario.filter(periodoprofesormodulo=query_ppm[0],
                            dia_semana=dia_semana)

        if query_horario.exists():
            print("existe")
            query_horario=query_horario.get()
            query_horario.bloque1=bloque1
            query_horario.bloque2=bloque2
            query_horario.bloque3=bloque3
            query_horario.bloque4=bloque4
            query_horario.bloque5=bloque5
            query_horario.bloque6=bloque6
            query_horario.bloque7=bloque7
            query_horario.bloque8=bloque8
            query_horario.bloque9=bloque9
            query_horario.bloque10=bloque10
            # query_horario.dia_semana=dia_semana
        else:
            print("no existe")
            query_horario=Horario(
                periodoprofesormodulo=query_ppm[0],
                bloque1=bloque1,
                bloque2=bloque2,
                bloque3=bloque3,
                bloque4=bloque4,
                bloque5=bloque5,
                bloque6=bloque6,
                bloque7=bloque7,
                bloque8=bloque8,
                bloque9=bloque9,
                bloque10=bloque10,
                dia_semana = dia_semana,
            )
        query_horario.save()

        return HttpResponse("Save")
    else:

        return redirect("/horario/add/")


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
