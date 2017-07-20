from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Max

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
                               Carrera,
                               Bloque,
                               Actividad,
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

import json
import collections

# Create your views here.

dic_dia_semana={"1": "Lunes",
                "2":"Martes",
                "3":"Miercoles",
                "4":"Jueves",
                "5":"Viernes",
                }

from parametros.views import StaffRequiredMixin


def create_dic_bloque():
    """
    Recibe como parametro un objeto de tipo Queryset->Bloque
    Creo diccionario con todos los elementos de la clase bloque.
    Esto crea dos elementos uno de tipo string (key) y otro el tipo
    diccionario (value), que a su vez contiene la key de bloque y value
    por defecto como falso.
    ejemplo, dic={key:value{xx:vv}}
    """
    dia_semana = collections.OrderedDict(sorted(dic_dia_semana.items()))
    b = Bloque.objects.all().order_by("nombre")

    dic={}

    for i in dia_semana:
        dic_aux={}

        for t in b:
            dic_aux[t]= False

        dic[i]=dic_aux

    dic = collections.OrderedDict(sorted(dic.items()))

    return dic


def create_dic_bloque_title(context):
    """
    Recibe: Context
    Crea los titulos y extensión de los bloques para ser dibujado en la tabla
    que realiza la interacción con el horario
    Retorna: Context
    """

    b = Bloque.objects.all().order_by("nombre")
    context["bloque_list"] = b

    #max de bloque
    b = b.aggregate(Max("nombre"))
    b = b["nombre__max"]
    context["bloque_max"] = range(0, b)

    return context


class PeriodoProfesorModuloListView(StaffRequiredMixin, ViewListView):
    model = PeriodoProfesorModulo
    template_name = "horario/base_horario.html"
    titulo = "Asignación Profesor Módulo"
    extra_context = {}


    def get_context_data(self, *args, **kwargs):

        context = super(PeriodoProfesorModuloListView, self).get_context_data(*args, **kwargs)

        periodo = self.request.GET.get("periodo")
        carrera = self.request.GET.get("carrera")
        plan = self.request.GET.get("plan")

        c = Carrera.objects.all().order_by("nombre")
        context['carrera'] = c

        if carrera is None or carrera == 0:
            queryset = None

        else:
            #habilito el select de periodo
            p = Periodo.objects.all().order_by("-nombre")
            context['periodo'] = p

            #habilito select de plan
            pl = Plan.objects.all().filter(carrera = carrera)
            pl = pl.order_by("-nombre")
            context["plan"] = pl

        if carrera is not None and carrera !=0:
            #filtro el query por carrera para ser listado
            queryset = PeriodoProfesorModulo.objects.all()
            queryset = queryset.filter(carrera=carrera)


        if periodo is not None and periodo !=0:
            # filtro el query por periodo
            # el resultando es de carrera + periodo
            queryset = queryset.filter(periodo=periodo)

        if plan is not None and plan !=0:
            #filtro el query por plan
            #el resultante es filtro de carrera + plan
            queryset = queryset.filter(plan=plan)


        context['object_list'] = queryset

        return context


class PeriodoProfesorModuloCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = PeriodoProfesorModuloForm
    template_name = "horario/form.html"
    titulo = "Agrega Asignacion de periodo-profesor-modulo"
    success_message = "La Asignacion %(nombre)s ha sido creado"
    success_url = "/periodoprofesormodulo/"


    def get_context_data(self, **kwargs):

        context = super(PeriodoProfesorModuloCreateView, self).get_context_data(**kwargs)

        dic=create_dic_bloque()

        context["horario"] = dic
        context["dia_semana_list"] = dic_dia_semana

        create_dic_bloque_title(context)

        return context


    def get_success_message(self, cleaned_data):
        """
        cleaned_data is the cleaned data from the form which is used for string
        formatting
        """
        return self.success_message % dict(cleaned_data,
                                       nombre=self.object.profesor.nombre)

    def form_valid(self, form):
        form.save()
        return super(PeriodoProfesorModuloCreateView, self).form_valid(form)


class PeriodoProfesorModuloUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = PeriodoProfesorModulo
    form_class = PeriodoProfesorModuloForm
    template_name = "horario/form.html"
    success_message = "El Profesor %(nombre)s ha sido actualizado"
    success_url = "/periodoprofesormodulo/"
    titulo = "Edita Asignacion de periodo-profesor-modulo"


    def get_context_data(self, **kwargs):

        context = super(PeriodoProfesorModuloUpdateView, self).get_context_data(**kwargs)
        context["dia_semana_list"] = dic_dia_semana

        h = None
        ppm = context["object"]

        if (ppm is not None):
            h = Horario.objects.all().filter(periodoprofesormodulo = ppm)
            h = h.order_by("dia_semana", "bloque__nombre")

        dic=create_dic_bloque()

        for i in h:
            """
            Actualizo los elementos del diccionario creado, esto es solo para
            los elementos que se encuentran en la clase horario.
            """
            x=dic[i.dia_semana]
            xx = x[i.bloque]=i.reservado

        #print(_a)
        context["horario"] = dic
        context = create_dic_bloque_title(context)
        create_dic_bloque_title(context)

        return context


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


    def get_context_data(self, *args, **kwargs):

        context = super(ReservaBloqueProtegidoListView, self).get_context_data(*args, **kwargs)

        bloque = Bloque.objects.all().order_by("nombre")
        context['bloque'] = bloque

        return context


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
        query = Periodo.objects.all().order_by("nombre")

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


@csrf_exempt
def GetCarrera(request):

    if request.method == "POST" and request.is_ajax():
        codigo = request.POST.get("codigo")
        query = Carrera.objects.all()
        query = query.order_by("nombre")

        return JsonResponse(serializers.serialize('json', query), safe=False)

@csrf_exempt
def GetActividad(request):

    if request.method == "POST" and request.is_ajax():
        codigo = request.POST.get("codigo")
        query = Actividad.objects.all()
        query = query.order_by("nombre")

        return JsonResponse(serializers.serialize('json', query), safe=False)


# para salvar actividad en cierto bloque
@csrf_exempt
def SaveActividadBloque(request):

    if request.method == "POST" and request.is_ajax():
        codigo = request.POST.get("codigo")
        s = Horario.objects.all()
        # query = query.order_by("nombre")

        s = s.filter(dia = dia_semana)
        s = s.filter(bloque = bloque)
        s = s.filter(ppm = periodoprofesormodulo)

        s.save()
        s.update()


    return HttpResponse("")


@csrf_exempt
def SaveHorarioProtegido(request):

    if request.method == "POST" and request.is_ajax():
        bloque = request.POST.get("bloque")
        value = request.POST.get("value")

        b = Bloque.objects.all()
        b = b.filter(nombre=bloque)


        r = ReservaBloqueProtegido.objects.all()
        r = r.filter(bloque = b[0])

        if value == "X":
            value = True
        else:
            value = False

        if not r.exists():
            r = r(
            bloque = b[0],
            reservado = value,
            )
            r.save()
        else:
            r.update(
                reservado = value
            )

    return HttpResponse("")


@csrf_exempt
def saveHorario(request):
    if request.method == "POST" and request.is_ajax():
        """
        POST trae como valores:
        row = Fila que refiere al día de la semana.
        col = Columna que referencia al bloque.
        value = Valor de texto de la celda clickeada.
        """

        actividad = request.POST.get("value")
        dia = request.POST.get("row")
        bloque = request.POST.get("bloque")

        print('BLOQUE: '+bloque)
        print(dia)

        valor = Actividad.objects.all()
        block = Bloque.objects.all()

       


        valor = valor.filter(identificador = actividad)
        #num = block.filter(id = bloque)
        block = block.filter(nombre = bloque)
        
       
        print("NOMBRE")
        print(block[0].nombre)

        #datos de periodo prof modulo
        periodo = request.POST.get("periodo")
        carrera = request.POST.get("carrera")
        plan = request.POST.get("plan")
        modulo = request.POST.get("modulo")
        profesor = request.POST.get("profesor")

        query = PeriodoProfesorModulo.objects.all()
        query = query.filter(periodo__id = periodo)
        query = query.filter(carrera__id= carrera)
        query = query.filter(plan__id= plan)
        query = query.filter(modulo__id= modulo)
        query = query.filter(profesor__id= profesor)
        
        a = Horario(periodoprofesormodulo = query[0], 
            dia_semana = dia,
            reservado = True,
            bloque = block[0],
            actividad = valor[0],
            )

        a.save()

        """
        if (value.upper() == "X"):
            value = True
        else:
            value = False
        """
        print(a)
        


    return HttpResponse("")
