from django.conf.urls import url
from .views import (
    DepartamentoView,
    CarreraView,
    PlanView,
    ModuloView,
    AnioView,
    PeriodoView,
    BloqueView,
    )

urlpatterns = [
    url(r'^departamento/$', DepartamentoView, name='departamento'),
    url(r'^carrera/$', CarreraView, name='Carrera'),
    url(r'^plan/$', PlanView, name='Plan'),
    url(r'^modulo/$', ModuloView, name='Modulo'),
    url(r'^anio/$', AnioView, name='Anio'),
    url(r'^periodo/$', PeriodoView, name='Periodo'),
    url(r'^bloque/$', BloqueView, name='Bloque'),
    #url(r'^sobrenosotros/$', sobre, name='sobre'),

] 
