from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import (
    DepartamentoForm,
    CarreraForm,
)

from .models import (
    Departamento,
    Carrera,
)


def DepartamentoView(request):

    titulo = "Departamento"

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

    titulo = "Carrera"

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
