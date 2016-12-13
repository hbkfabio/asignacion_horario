from django.conf.urls import url
from .views import (
    CarreraView,
    CarreraCreateView,
    CarreraUpdateView,
    CarreraDeleteView,
    PlanView,
    PlanCreateView,
    PlanUpdateView,
    PlanDeleteView,
    ModuloView,
    ModuloCreateView,
    ModuloUpdateView,
    ModuloDeleteView,
    DepartamentoView,
    DepartamentoCreateView,
    DepartamentoUpdateView,
    DepartamentoDeleteView,
    AnioView,
    AnioCreateView,
    AnioUpdateView,
    AnioDeleteView,
    PeriodoView,
    PeriodoCreateView,
    PeriodoUpdateView,
    PeriodoDeleteView,
    BloqueView,
    BloqueCreateView,
    BloqueUpdateView,
    BloqueDeleteView,
    ProfesorView,
    ProfesorUpdateView,
    ProfesorCreateView,
    ProfesorDeleteView
    )

urlpatterns = [
    #carrera
    url(r'^carrera/$', CarreraView.as_view(), name='carrera-list'),
    url(r'^carrera/add/$', CarreraCreateView.as_view(), name='carrera-add'),
    url(r'^carrera/edit/(?P<pk>\d+)/$', CarreraUpdateView.as_view(), name='carrera-edit'),
    url(r'^carrera/(?P<pk>\d+)/delete/$', CarreraDeleteView.as_view(), name='carrera-delete'),
    #plan
    url(r'^plan/$', PlanView.as_view(), name='plan-list'),
    url(r'^plan/add/$', PlanCreateView.as_view(), name='plan-add'),
    url(r'^plan/edit/(?P<pk>\d+)/$', PlanUpdateView.as_view(), name='plan-edit'),
    url(r'^plan/(?P<pk>\d+)/delete/$', PlanDeleteView.as_view(), name='plan-delete'),
    #modulo
    url(r'^modulo/$', ModuloView.as_view(), name='modulo-list'),
    url(r'^modulo/add/$', ModuloCreateView.as_view(), name='modulo-add'),
    url(r'^modulo/edit/(?P<pk>\d+)/$', ModuloUpdateView.as_view(), name='modulo-edit'),
    url(r'^modulo/(?P<pk>\d+)/delete/$', ModuloDeleteView.as_view(), name='modulo-delete'),
    #departamento
    url(r'^departamento/$', DepartamentoView.as_view(), name='departamento-list'),
    url(r'^departamento/add/$', DepartamentoCreateView.as_view(), name='departamento-add'),
    url(r'^departamento/edit/(?P<pk>\d+)/$', DepartamentoUpdateView.as_view(), name='departamento-edit'),
    url(r'^departamento/(?P<pk>\d+)/delete/$', DepartamentoDeleteView.as_view(), name='departamento-delete'),
    #año
    url(r'^anio/$', AnioView.as_view(), name='anio-list'),
    url(r'^anio/add/$', AnioCreateView.as_view(), name='anio-add'),
    url(r'^anio/edit/(?P<pk>\d+)/$', AnioUpdateView.as_view(), name='anio-edit'),
    url(r'^anio/(?P<pk>\d+)/delete/$', AnioDeleteView.as_view(), name='anio-delete'),
    #Periodo
    url(r'^periodo/$', PeriodoView.as_view(), name='periodo-list'),
    url(r'^periodo/add/$', PeriodoCreateView.as_view(), name='periodo-add'),
    url(r'^periodo/edit/(?P<pk>\d+)/$', PeriodoUpdateView.as_view(), name='periodo-edit'),
    url(r'^periodo/(?P<pk>\d+)/delete/$', PeriodoDeleteView.as_view(), name='periodo-delete'),
    #bloque
    url(r'^bloque/$', BloqueView.as_view(), name='bloque-list'),
    url(r'^bloque/add/$', BloqueCreateView.as_view(), name='bloque-add'),
    url(r'^bloque/edit/(?P<pk>\d+)/$', BloqueUpdateView.as_view(), name='bloque-edit'),
    url(r'^bloque/(?P<pk>\d+)/delete/$', ProfesorDeleteView.as_view(), name='bloque-delete'),
    #profesor
    url(r'^profesor/$', ProfesorView.as_view(), name='profesor-list'),
    url(r'^profesor/add/$', ProfesorCreateView.as_view(), name='profesor-add'),
    url(r'^profesor/edit/(?P<pk>\d+)/$', ProfesorUpdateView.as_view(), name='profesor-edit'),
    url(r'^profesor/(?P<pk>\d+)/delete/$', ProfesorDeleteView.as_view(), name='profesor-delete'),

] 
