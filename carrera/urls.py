from django.conf.urls import url
from .views import (
    DepartamentoView,
    CarreraView,
    PlanView,
    ModuloView,
    AnioView,
    PeriodoView,
    BloqueView,
    BloqueCreateView,
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
    # url(r'^bloque/$', BloqueView, name='Bloque'),
    url(r'^bloque/$', BloqueView.as_view(), name='Bloque'),
    url(r'^bloque/add/$', BloqueCreateView.as_view(), name='Bloque_add'),
    url(r'^bloque/?P<pk>\d+/$', BloqueUpdateView.as_view(), name='Bloque_update'),
    url(r'^bloque/(?P<pk>\d+)/delete/$', ProfesorDeleteView.as_view(), name='Bloque_delete'),
    url(r'^profesor/$', ProfesorView.as_view(), name='Profesor'),
    url(r'^profesor/add/$', ProfesorCreateView.as_view(), name='Profesor_add'),
    url(r'^profesor/(?P<pk>\d+)/$', ProfesorUpdateView.as_view(), name='Profesor_update'),
    url(r'^profesor/(?P<pk>\d+)/delete/$', ProfesorDeleteView.as_view(), name='Profesor_delete'),
    #url(r'^sobrenosotros/$', sobre, name='sobre'),

] 
