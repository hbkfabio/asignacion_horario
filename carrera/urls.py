from django.conf.urls import url
from .views import (
    DepartamentoView,
    CarreraView,
    )

urlpatterns = [
    url(r'^departamento/$', DepartamentoView, name='departamento'),
    url(r'^carrera/$', CarreraView, name='Carrera'),
    #url(r'^sobrenosotros/$', sobre, name='sobre'),

] 
