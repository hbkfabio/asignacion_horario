from django.conf.urls import url
from .views import (
    DepartamentoView,
    CarreraView,
    PlanView,
    ModuloView,
    AnioView,
    PeriodoView,
    )

urlpatterns = [
    url(r'^departamento/$', DepartamentoView, name='departamento'),
    url(r'^carrera/$', CarreraView, name='Carrera'),
    url(r'^plan/$', PlanView, name='Plan'),
    url(r'^modulo/$', ModuloView, name='Modulo'),
    url(r'^anio/$', AnioView, name='Anio'),
    url(r'^periodo/$', PeriodoView, name='Periodo'),
    #url(r'^sobrenosotros/$', sobre, name='sobre'),

] 
