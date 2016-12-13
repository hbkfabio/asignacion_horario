from django.conf.urls import url
from .views import (
    CarreraView,
    PlanView,
    ModuloView,
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
    url(r'^carrera/$', CarreraView, name='Carrera'),
    url(r'^plan/$', PlanView, name='Plan'),
    url(r'^modulo/$', ModuloView, name='Modulo'),
    #departamento
    url(r'^departamento/$', DepartamentoView.as_view(), name='departamento'),
    url(r'^departamento/add/$', DepartamentoCreateView.as_view(), name='departamento_add'),
    url(r'^departamento/edit/(?P<pk>\d+)/$', DepartamentoUpdateView.as_view(), name='departamento_edit'),
    url(r'^departamento/(?P<pk>\d+)/delete/$', DepartamentoDeleteView.as_view(), name='departamento_delete'),
    #año
    url(r'^anio/$', AnioView.as_view(), name='anio'),
    url(r'^anio/add/$', AnioCreateView.as_view(), name='anio_add'),
    url(r'^anio/edit/(?P<pk>\d+)/$', AnioUpdateView.as_view(), name='anio_edit'),
    url(r'^anio/(?P<pk>\d+)/delete/$', AnioDeleteView.as_view(), name='anio_edit'),
    #Periodo
    url(r'^periodo/$', PeriodoView.as_view(), name='periodo'),
    url(r'^periodo/add/$', PeriodoCreateView.as_view(), name='periodo_add'),
    url(r'^periodo/edit/(?P<pk>\d+)/$', PeriodoUpdateView.as_view(), name='periodo_edit'),
    url(r'^periodo/(?P<pk>\d+)/delete/$', PeriodoDeleteView.as_view(), name='periodo_delete'),
    #bloque
    url(r'^bloque/$', BloqueView.as_view(), name='bloque'),
    url(r'^bloque/add/$', BloqueCreateView.as_view(), name='bloque_add'),
    url(r'^bloque/edit/(?P<pk>\d+)/$', BloqueUpdateView.as_view(), name='bloque_edit'),
    url(r'^bloque/(?P<pk>\d+)/delete/$', ProfesorDeleteView.as_view(), name='bloque_delete'),
    #profesor
    url(r'^profesor/$', ProfesorView.as_view(), name='profesor'),
    url(r'^profesor/add/$', ProfesorCreateView.as_view(), name='profesor_add'),
    url(r'^profesor/edit/(?P<pk>\d+)/$', ProfesorUpdateView.as_view(), name='profesor_edit'),
    url(r'^profesor/(?P<pk>\d+)/delete/$', ProfesorDeleteView.as_view(), name='profesor_delete'),
    #url(r'^sobrenosotros/$', sobre, name='sobre'),

] 
