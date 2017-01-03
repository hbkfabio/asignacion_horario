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
    SemestreForm,
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
    Semestre,
)


from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
	@method_decorator(staff_member_required)
	def dispatch(self, request, *args, **kwargs):
		return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


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


class CarreraView(StaffRequiredMixin, ViewListView):
    model = Carrera
    template_name = "parametros/maestro.html"
    titulo = "Carreras"
    extra_context = {}


class CarreraCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = CarreraForm
    template_name = "parametros/form.html"
    titulo = "Agrega Carrera"
    success_message = "La carrera %(nombre)s ha sido creado"
    success_url = "/carrera/"


class CarreraUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = "parametros/form.html"
    success_message = "La carrera %(name)s ha sido actualizado"
    success_url = "/carrera/"


class CarreraDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = Carrera
    template_name = "parametros/elimina.html"
    success_message = 'La carrera %(nombre)s ha sido Eliminada'
    success_url = "/carrera/"


class PlanView(StaffRequiredMixin, ViewListView):
    model = Plan
    template_name = "parametros/maestro.html"
    titulo = "Planes"
    extra_context = {}


class PlanCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = PlanForm
    template_name = "parametros/form.html"
    titulo = "Agrega Plan"
    success_message = "El Plan %(nombre)s ha sido creado"
    success_url = "/plan/"


class PlanUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = Plan
    form_class = PlanForm
    template_name = "parametros/form.html"
    success_message = "El Plan %(name)s ha sido actualizado"
    success_url = "/plan/"


class PlanDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = Plan
    template_name = "parametros/elimina.html"
    success_message = 'El Plan %(nombre)s ha sido Eliminado'
    success_url = "/plan/"


class ModuloView(StaffRequiredMixin, ViewListView):
    model = Modulo
    template_name = "parametros/maestro.html"
    titulo = "Modulos"
    extra_context = {}


class ModuloCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = ModuloForm
    template_name = "parametros/form.html"
    titulo = "Agrega Modulo"
    success_message = "El Modulo %(nombre)s ha sido creado"
    success_url = "/modulo/"


class ModuloUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = Modulo
    form_class = ModuloForm
    template_name = "parametros/form.html"
    success_message = "El Modulo %(name)s ha sido actualizado"
    success_url = "/modulo/"


class ModuloDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = Modulo
    template_name = "parametros/elimina.html"
    success_message = 'El Modulo %(nombre)s ha sido Eliminado'
    success_url = "/modulo/"


class DepartamentoView(StaffRequiredMixin, ViewListView):
    model = Departamento
    template_name = "parametros/maestro.html"
    titulo = "Departamentos"
    extra_context = {}


class DepartamentoCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = DepartamentoForm
    template_name = "parametros/form.html"
    titulo = "Agrega Departamento"
    success_message = "El Departamento %(nombre)s ha sido creado"
    success_url = "/departamento"


class DepartamentoUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = "parametros/form.html"
    success_message = "El Departamento %(name)s ha sido actualizado"
    success_url = "/departamento"


class DepartamentoDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = Departamento
    template_name = "parametros/elimina.html"
    success_message = 'El Departamento %(nombre)s ha sido Eliminado'
    success_url = "/departamento"

class AnioView(ViewListView):
    model = Anio
    template_name = "parametros/maestro.html"
    titulo = "Años"
    extra_context = {}


class AnioCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = AnioForm
    template_name = "parametros/form.html"
    titulo = "Agrega Año"
    success_message = "El Año %(nombre)s ha sido creado"
    success_url = "/anio"


class AnioUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = Anio
    form_class = AnioForm
    template_name = "parametros/form.html"
    success_message = "El Año %(name)s ha sido actualizado"
    success_url = "/anio"


class AnioDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = Anio
    template_name = "parametros/elimina.html"
    success_message = 'El Año %(nombre)s ha sido Eliminado'
    success_url = "/anio"


class PeriodoView(StaffRequiredMixin, ViewListView):
    model = Periodo
    template_name = "parametros/maestro.html"
    titulo = "Periodos"
    extra_context = {}


class PeriodoCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = PeriodoForm
    template_name = "parametros/form.html"
    titulo = "Agrega Periodo"
    success_message = "El Periodo %(nombre)s ha sido creado"
    success_url = "/periodo"


class PeriodoUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = Periodo
    form_class = PeriodoForm
    template_name = "parametros/form.html"
    success_message = "El Periodo %(nombre)s ha sido actualizado"
    success_url = "/periodo"


class PeriodoDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = Periodo
    template_name = "parametros/elimina.html"
    success_message = 'El Periodo %(nombre)s ha sido Eliminado'
    success_url = "/periodo"


class BloqueView(StaffRequiredMixin, ViewListView):
    model = Bloque
    template_name = "parametros/maestro.html"
    titulo = "Bloques"
    extra_context = {}


class BloqueCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = BloqueForm
    template_name = "parametros/form.html"
    titulo = "Agrega Bloques"
    success_message = "El Bloque %(nombre)s ha sido creado"
    success_url = "/bloque"


class BloqueUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = Bloque
    form_class = BloqueForm
    template_name = "parametros/form.html"
    success_message = "El Bloque %(name)s ha sido actualizado"
    success_url = "/bloque"


class BloqueDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = Bloque
    template_name = "parametros/elimina.html"
    success_message = 'Bloque %(nombre)s ha sido Eliminado'
    success_url = "/bloque"


class ProfesorView(StaffRequiredMixin, ViewListView):
    model = Profesor
    template_name = "parametros/maestro.html"
    titulo = "Profesores"
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ProfesorView, self).get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context


class ProfesorCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = ProfesorForm
    template_name = "parametros/form.html"
    success_message = 'Profesor %(nombre)s ha sido creado'
    titulo = 'Agregar Profesor'
    success_url = '/profesor/'


class ProfesorUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = "parametros/form.html"
    success_message = "Profesor %(nombre)s ha sido actualizado"
    success_url = "/profesor/"



class ProfesorDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = Profesor
    template_name = "parametros/elimina.html"
    success_message = 'Profesor %(nombre)s ha sido Eliminado'
    success_url = "/profesor/"

class SemestreView(StaffRequiredMixin, ViewListView):
    model = Semestre
    template_name = "parametros/maestro.html"
    titulo = "Semestres"
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(SemestreView, self).get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context


class SemestreCreateView(StaffRequiredMixin, ViewCreateView):
    form_class = SemestreForm
    template_name = "parametros/form.html"
    success_message = 'El semestre %(nombre)s ha sido creado'
    titulo = 'Agregar Semestre'
    success_url = '/semestre/'


class SemestreUpdateView(StaffRequiredMixin, ViewUpdateView):
    model = Semestre
    form_class = SemestreForm
    template_name = "parametros/form.html"
    success_message = "El semestre %(nombre)s ha sido actualizado"
    success_url = "/semestre/"



class SemestreDeleteView(StaffRequiredMixin, ViewDeleteView):
    model = Semestre
    template_name = "parametros/elimina.html"
    success_message = 'El semestre %(nombre)s ha sido Eliminado'
    success_url = "/semestre/"
