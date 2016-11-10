from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import (
    DepartamentoForm,
    CarreraForm,
    PlanForm,
    ModuloForm,
    AnioForm,
    PeriodoForm,
    BloqueForm,
    ProfesorForm,
)

from .models import (
    Departamento,
    Carrera,
    Plan,
    Modulo,
    Anio,
    Periodo,
    Bloque,
    Profesor,
)


def DepartamentoView(request):

    titulo = "Departamentos"

    form = DepartamentoForm(request.POST or None, request.FILES or None)

    queryset = Departamento.objects.all().order_by("nombre")

    context = {
            "titulo": titulo,
            "form": form,
            "queryset": queryset
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.INFO, "Se ha guardado %s" %instance.nombre)
        return HttpResponseRedirect("/departamento/")

    return render(request, "maestro.html", context)


def CarreraView(request):

    titulo = "Carreras"

    template = "maestro.html"

    form = CarreraForm(request.POST or None, request.FILES or None)

    queryset = Carrera.objects.all().order_by('nombre')

    context = {
        "titulo": titulo,
        "form": form,
        "queryset": queryset,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.INFO, "Se ha guardado %s" %instance.nombre)
        #return redirect("/carrera/")
        return HttpResponseRedirect("carrera")

    return render(request,template, context)

def PlanView(request):

    titulo = "Planes"

    template = "maestro.html"

    form = PlanForm(request.POST or None, request.FILES or None)

    queryset = Plan.objects.all().order_by("id")


    context = {
        "titulo":titulo,
        "form":form,
        "queryset":queryset,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.INFO,
        "Se ha guardado %s para la carrera %s"%
                             (instance.nombre,
                              instance.carrera.nombre)
                             )
        return HttpResponseRedirect("/plan/")


    return render(request, template, context)


def ModuloView(request):

    titulo = "Modulos"

    template = "maestro.html"

    form = ModuloForm(request.POST or None, request.FILES or None)

    queryset = Modulo.objects.all().order_by("id")


    context = {
        "titulo":titulo,
        "form":form,
        "queryset":queryset,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.INFO,
        "Se ha guardado %s para el plan %s"%
                             (instance.nombre,
                              instance.plan.nombre)
                             )
        return HttpResponseRedirect("/modulo/")

    return render(request, template, context)



def AnioView(request):

    titulo = "Años"

    template = "maestro.html"

    form = AnioForm(request.POST or None, request.FILES or None)

    queryset = Anio.objects.all().order_by("id")


    context = {
        "titulo":titulo,
        "form":form,
        "queryset":queryset,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.INFO,
        "Se ha guardado el año %s "
                             %(instance.nombre,
                             )
                             )
        return HttpResponseRedirect("/anio/")

    return render(request, template, context)


def PeriodoView(request):

    titulo = "Periodos"

    template = "maestro.html"

    form = PeriodoForm(request.POST or None, request.FILES or None)

    queryset = Periodo.objects.all().order_by("id")


    context = {
        "titulo":titulo,
        "form":form,
        "queryset":queryset,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.INFO,
        "Se ha guardado el periodo %s para el Año %s"
                            %(instance.nombre,
                             instance.anio.nombre)
                             )
        return HttpResponseRedirect("/anio/")

    return render(request, template, context)


def BloqueView(request):

    titulo = "Bloques"

    template = "maestro.html"

    form = BloqueForm(request.POST or None, request.FILES or None)

    queryset = Bloque.objects.all().order_by("id")


    context = {
        "titulo":titulo,
        "form":form,
        "queryset":queryset,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.INFO,
        "Se ha guardado el %s %s "
                             %(titulo,
                             instance.nombre,
                             )
                            )
        return HttpResponseRedirect("/bloque/")

    return render(request, template, context)


def ProfesorView(request):

    titulo = "Profesores"

    template = "maestro.html"

    form = ProfesorForm(request.POST or None, request.FILES or None)

    queryset = Profesor.objects.all().order_by("id")


    context = {
        "titulo":titulo,
        "form":form,
        "queryset":queryset,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.INFO,
        "Se ha guardado al profesor %s "
                             %(instance.nombre,
                             )
                            )
        return HttpResponseRedirect("/profesor/")

    return render(request, template, context)

