from django.conf.urls import url
from .views import (
    DepartamentoView,
    CarreraView,
    PlanView,
    ModuloView,
    AnioView,
    PeriodoView,
    BloqueView,
    ProfesorView,
    ProfesorUpdateView,
    ProfesorCreateView,
    ProfesorDeleteView
    )

urlpatterns = [
    url(r'^departamento/$', DepartamentoView, name='departamento'),
    url(r'^carrera/$', CarreraView, name='Carrera'),
    url(r'^plan/$', PlanView, name='Plan'),
    url(r'^modulo/$', ModuloView, name='Modulo'),
    url(r'^anio/$', AnioView, name='Anio'),
    url(r'^periodo/$', PeriodoView, name='Periodo'),
    url(r'^bloque/$', BloqueView, name='Bloque'),
    url(r'^profesor/$', ProfesorView.as_view(), name='Profesor'),
    url(r'^profesor/crear/$', ProfesorCreateView.as_view(), name='Profesor-crear'),
    url(r'^profesor/(?P<pk>\d+)/update/$', ProfesorUpdateView.as_view(), name='Profesor-update'),
    #url(r'^profesor/(?P<pk>\d+)/actuliza/$', ProfesorUpdateView.as_view(), name='Profesor-actuliza'),
    url(r'^profesor/(?P<pk>\d+)/elimina/$', ProfesorDeleteView.as_view(), name='Profesor-elimina'),
    #url(r'^sobrenosotros/$', sobre, name='sobre'),

] 
