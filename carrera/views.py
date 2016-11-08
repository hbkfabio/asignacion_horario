from django.shortcuts import render

from .forms import DepartamentoForm


def DepartamentoView(request):

    titulo = "Departamento"

    form = DepartamentoForm(request.POST or None, request.FILES or None)

    context = {
            "titulo": titulo,
            "form": form,
    }

    return render(request, "maestro.html", context)
