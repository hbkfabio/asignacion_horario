from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import (DepartamentoForm,
                CarreraForm,
                )


def DepartamentoView(request):

    titulo = "Departamento"

    form = DepartamentoForm(request.POST or None, request.FILES or None)

    context = {
            "titulo": titulo,
            "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance)

    return render(request, "maestro.html", context)


def CarreraView(request):

    titulo = "Carrera"

    form = CarreraForm(request.POST or None, request.FILES or None)

    context = {
        "titulo": titulo,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/carrera/")
        #return redirect(instance)

    return render(request, "maestro.html", context)
