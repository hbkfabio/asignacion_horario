from django.conf.urls import url
from .views import (
    DepartamentoView,
    CarreraView,
    PlanView,
    )

urlpatterns = [
    url(r'^departamento/$', DepartamentoView, name='departamento'),
    url(r'^carrera/$', CarreraView, name='Carrera'),
    url(r'^plan/$', PlanView, name='Plan')
    #url(r'^sobrenosotros/$', sobre, name='sobre'),

] 
