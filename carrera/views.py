from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin


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


# def BloqueView(request):

#     titulo = "Bloques"

#     template = "maestro.html"

#     form = BloqueForm(request.POST or None, request.FILES or None)

#     queryset = Bloque.objects.all().order_by("id")


#     context = {
#         "titulo":titulo,
#         "form":form,
#         "queryset":queryset,
#     }

#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         messages.add_message(request, messages.INFO,
#         "Se ha guardado el %s %s "
#                              %(titulo,
#                              instance.nombre,
#                              )
#                             )
#         return HttpResponseRedirect("/bloque/")

#     return render(request, template, context)


# class BloqueView(ListView):
#     model = Bloque
#     template_name = "maestro.html"
#     titulo = "Bloques"
#     extra_context = {}

#     def get_context_data(self, **kwargs):
#         context = super(BloqueView, self).get_context_data(*kwargs)
#         context['titulo'] = self.titulo
#         return context



# class BloqueCreateView(SuccessMessageMixin, CreateView):
#     form_class = BloqueForm
#     template_name = "profesor_form.html"
#     titulo = "Agrega Bloques"
#     success_message = "El Bloque %(nombre)s ha sido creado"


#     def get_context_data(self, **kwargs):
#         context = super(BloqueCreateView, self).get_context_data(*kwargs)
#         context['titulo'] = self.titulo
#         return context


#     def get_success_url(self):
#         return reverse("Bloque")

#     def get_success_message(self, cleaned_data):
    #cleaned_data is the cleaned data from the form which is used for string formatting
#         return self.success_message % dict(cleaned_data,
#                                        nombre=self.object.nombre)


class ViewListView(ListView):
    model = None
    template_name = None
    titulo = None
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ViewListView, self).get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context



class ViewCreateView(SuccessMessageMixin, CreateView):
    form_class = None
    template_name = None
    success_message = None
    titulo = None


    def get_context_data(self, **kwargs):
        context = super(ViewCreateView, self).get_context_data(*kwargs)
        context['titulo'] = self.titulo
        return context


    def get_success_message(self, cleaned_data):
    #cleaned_data is the cleaned data from the form which is used for string formatting
        return self.success_message % dict(cleaned_data,
                                       nombre=self.object.nombre)



class ViewUpdateView(SuccessMessageMixin, UpdateView):
    model = None
    form_class = None
    template_name = None
    success_message = None
    titulo = None


    def get_context_data(self, **kwargs):
        context = super(ViewUpdateView, self).get_context_data(*kwargs)
        context['titulo'] = self.titulo
        return context


    def get_success_message(self, cleaned_data):
        # print (_a)
        return self.success_message % dict(cleaned_data,
                                       nombre=self.object.nombre)



class ViewDeleteView(SuccessMessageMixin, DeleteView):
    model = None
    template_name = None
    success_message = None


    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message %dict(nombre=obj,))
        return super(ViewDeleteView, self).delete(request, *args, **kwargs)


class BloqueView(ViewListView):
    model = Bloque
    template_name = "maestro.html"
    titulo = "Bloques"
    extra_context = {}


class BloqueCreateView(ViewCreateView):
    form_class = BloqueForm
    template_name = "profesor_form.html"
    titulo = "Agrega Bloques"
    success_message = "El Bloque %(nombre)s ha sido creado"
    success_url = "/bloque"


class BloqueUpdateView(ViewUpdateView):
    model = Bloque
    form_class = BloqueForm
    template_name = "profesor_form.html"
    success_message = "El Bloque %(name)s ha sido actualizado"
    sucess_url = "/bloque"


class BloqueDeleteView(ViewDeleteView):
    model = Bloque
    template_name = "elimina.html"
    success_message = 'Bloque %(nombre)s ha sido Eliminado'
    sucess_url = "/bloque"


class ProfesorView(ViewListView):
    model = Profesor
    template_name = "maestro.html"
    titulo = "Profesores"
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ProfesorView, self).get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context



class ProfesorCreateView(ViewCreateView):
    form_class = ProfesorForm
    template_name = "profesor_form.html"
    success_message = 'Profesor %(nombre)s ha sido creado'
    titulo = 'Agregar Profesor'
    success_url = '/profesor'


class ProfesorUpdateView(ViewUpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = "profesor_form.html"
    success_message = "Profesor %(nombre)s ha sido actualizado"
    success_url = "/profesor"



class ProfesorDeleteView(ViewDeleteView):
    model = Profesor
    template_name = "elimina.html"
    success_message = 'Profesor %(nombre)s ha sido Eliminado'
    sucess_url = "/profesor"


