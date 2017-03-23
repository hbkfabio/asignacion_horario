from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from parametros.views import (ViewListView,
                            ViewCreateView,
                            ViewUpdateView,
                            ViewDeleteView,
                            )

from .models import (PeriodoProfesorModulo,
                     Horario,
                     ReservaBloqueProtegido,
                     )

from parametros.models import (Periodo,
                               Plan,
                               Profesor,
                               Modulo,
                               )

from .forms import (PeriodoProfesorModuloForm,
                    ReservaBloqueProtegidoForm,
                    )

from django.views.generic.base import TemplateView

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .valida import (valida_cantidad_horas,
                     valida_choque_horario,
                     )

import simplejson as json
import collections
# Create your views here.

dic_dia_semana={"1": "Lunes",
                "2":"Martes",
                "3":"Miercoles",
                "4":"Jueves",
                "5":"Viernes",
                }

from parametros.views import StaffRequiredMixin

class PeriodoProfesorModuloListView(StaffRequiredMixin, ViewListView):
    model = PeriodoProfesorModulo
    template_name = "horario/base_horario.html"
    titulo = "Asignación Profesor Módulo"
    extra_context = {}


class PeriodoProfesorModuloCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = PeriodoProfesorModuloForm
    template_name = "horario/form.html"
    titulo = "Agrega Asignacion de periodo-profesor-modulo"
    success_message = "La Asignacion %(nombre)s ha sido creado"
    success_url = "/periodoprofesormodulo/"


    def get_success_message(self, cleaned_data):
    #cleaned_data is the cleaned data from the form which is used for string formatting
        return self.success_message % dict(cleaned_data,
                                       nombre=self.object.profesor.nombre)

    def form_valid(self, form):
        form.save()
        # for i in sorted(dic_dia_semana, key=dic_dia_semana.get, reverse=False):
        #     horario = Horario(periodoprofesormodulo=PeriodoProfesorModulo.objects.latest('id'),
        #                       dia_semana=dic_dia_semana[i])
        #     horario.save()

        bloque_protegido = ReservaBloqueProtegido.objects.all()
        bloque1=""
        bloque2=""
        bloque3=""
        bloque4=""
        bloque5=""
        bloque6=""
        bloque7=""
        bloque8=""
        bloque9=""
        bloque10=""
        for i in bloque_protegido:
            if i.bloque1 == True:
                bloque1 = "X"
            if i.bloque2 == True:
                bloque2 = "X"
            if i.bloque3 == True:
                bloque3 = "X"
            if i.bloque4 == True:
                bloque4 = "X"
            if i.bloque5 == True:
                bloque5 = "X"
            if i.bloque6 == True:
                bloque6 = "X"
            if i.bloque7 == True:
                bloque7 = "X"
            if i.bloque8 == True:
                bloque8 = "X"
            if i.bloque9 == True:
                bloque9 = "X"
            if i.bloque10 == True:
                bloque10 = "X"

        dia_semana = collections.OrderedDict(sorted(dic_dia_semana.items()))
        for i in dia_semana:



            horario = Horario(periodoprofesormodulo=PeriodoProfesorModulo.objects.latest('id'),
                               dia_semana=i,
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
                               )
            horario.save()
        return super(PeriodoProfesorModuloCreateView, self).form_valid(form)


class PeriodoProfesorModuloUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = PeriodoProfesorModulo
    form_class = PeriodoProfesorModuloForm
    template_name = "horario/form.html"
    success_message = "El Profesor %(nombre)s ha sido actualizado"
    success_url = "/periodoprofesormodulo/"


    def get_success_message(self, cleaned_data):
    #cleaned_data is the cleaned data from the form which is used for string formatting
        return self.success_message % dict(cleaned_data,
                                       nombre=self.object.profesor.nombre)



class PeriodoProfesorModuloDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = PeriodoProfesorModulo
    template_name = "parametros/elimina.html"
    success_message = 'El Profesor %(nombre)s ha sido Eliminado'
    success_url = "/periodoprofesormodulo/"


    # def delete(self, request, *args, **kwargs):
    #     object = self.get_object()
    #     messages.success(self.request, self.success_message %dict(nombre=object,))
    #     return super(PeriodoProfesorModuloDeleteView, self).delete(request, *args, **kwargs)



class ReservaBloqueProtegidoListView(StaffRequiredMixin, ViewListView):
    model = ReservaBloqueProtegido
    template_name = "horario/base_horario.html"
    titulo = "Reserva Bloques protegidos Módulo"
    extra_context = {}


class ReservaBloqueProtegidoCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = ReservaBloqueProtegidoForm
    template_name = "horario/form.html"
    titulo = "Agrega Reserva de Bloque Protegido"
    success_message = "Se han reservado los bloques"
    success_url = "/reservabloqueprotegido/"


    def get_success_message(self, cleaned_data):
    #cleaned_data is the cleaned data from the form which is used for string formatting
        return self.success_message



class ReservaBloqueProtegidoUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = ReservaBloqueProtegido
    form_class = ReservaBloqueProtegido
    template_name = "horario/form.html"
    success_message = "Se han Actualizado los bloques"
    success_url = "/reservabloqueprotegido/"


    def get_success_message(self, cleaned_data):
    #cleaned_data is the cleaned data from the form which is used for string formatting
        return self.success_message


class ReservaBloqueProtegidoDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = ReservaBloqueProtegido
    template_name = "parametros/elimina.html"
    success_message = 'Se han eliminado los bloques protegidos'
    success_url = "/reservabloqueprotegido/"


    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message %dict(nombre=obj,))
        return super(ViewDeleteView, self).delete(request, *args, **kwargs)



class HorarioListView(StaffRequiredMixin, ViewListView):
    #queryset = Periodo.objects.all().order_by("-id")

    template_name = "horario/base_horario.html"
    titulo = "Listado de Horarios"
    # extra_context = {}

    # def get_context_data(self, **kwargs):
    #     context = super(HorarioListView, self).get_context_data(**kwargs)
    #     context["titulo"] = "Listado de Horarios"
    #     return context

    def get_queryset(self):
        return Periodo.objects.all().order_by("-id")


class HorarioTemplateView(StaffRequiredMixin, TemplateView):
    #edit
    template_name = "horario/base_horario.html"

    def get_context_data(self, **kwargs):

        periodo = self.request.GET.get("periodo")
        context = super(HorarioTemplateView, self).get_context_data(**kwargs)
        context["titulo"] = "Horario"

        dia_semana = collections.OrderedDict(sorted(dic_dia_semana.items()))
        context["dia_semana"] = dia_semana

        queryset = Horario.objects.all()

        if periodo is not None or periodo !="0":
            queryset =queryset.filter(periodoprofesormodulo__periodo=periodo)
            if not queryset:
                queryset = PeriodoProfesorModulo.objects.all().filter(periodo=periodo)
            context["queryset_profesor_modulo"] = queryset
        context["queryset_periodo"] = Periodo.objects.all().order_by('-id')
        return context


@csrf_exempt
def HorarioSave(request):

    if request.method == "POST" and request.is_ajax():
        model = Horario
        dic = request.POST.get("diccionario")
        dic = json.loads(dic)
        valor = request.POST.get("valor") #ultimo valor insertado
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
        semestre = dic["semestre"]
        dia_semana = dic["dia_semana"]
        titulo_bloque = dic["titulo_bloque"]

        query_ppm = PeriodoProfesorModulo.objects.all().filter(
                        profesor__nombre=profesor,
                        modulo__nombre=modulo,
                        modulo__plan__nombre = plan,
        )


        query_horario = Horario.objects.all()
        query_horario_ppm = query_horario.filter(periodoprofesormodulo=query_ppm[0])

        validar, msj = valida_cantidad_horas(query_horario_ppm, valor)

        if validar is False:
            return HttpResponse(msj)

        validar1, msj = valida_choque_horario(dia_semana, titulo_bloque,
                                            query_ppm[0].periodo,
                                            query_ppm[0].modulo.semestre,
                                            valor,
                                            )
        if validar1 is False:
            return HttpResponse(msj)

        if validar and validar1:
            # if valida:
            #     if validar1:
            #         msj = msj1
            query_horario = query_horario_ppm.filter(dia_semana=dia_semana)
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
            return HttpResponse(msj)
        else:

            return HttpResponse(msj)
            #return redirect("/horario/add/")

    else:
        return redirect("/horario/add/")


@csrf_exempt
def GetPlan(request):

    if request.method == "POST" and request.is_ajax():
        codigo = request.POST.get("codigo")
        query = Plan.objects.all().filter(carrera__id=codigo)
        query = query.order_by("-id")

        return JsonResponse(serializers.serialize('json', query), safe=False)


@csrf_exempt
def GetPeriodo(request):

    if request.method == "POST" and request.is_ajax():
        #codigo = request.POST.get("codigo")
        query = Periodo.objects.all().order_by("-id")

        return JsonResponse(serializers.serialize('json', query), safe=False)


@csrf_exempt
def GetProfesor(request):

    if request.method == "POST" and request.is_ajax():
        #codigo = request.POST.get("codigo")
        query = Profesor.objects.all().order_by("-id")

        return JsonResponse(serializers.serialize('json', query), safe=False)


@csrf_exempt
def GetModulo(request):

    if request.method == "POST" and request.is_ajax():
        codigo = request.POST.get("codigo")
        query = Modulo.objects.all().filter(plan__id = codigo)
        query = query.order_by("-id")

        return JsonResponse(serializers.serialize('json', query), safe=False)
