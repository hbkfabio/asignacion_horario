from django.conf.urls import url
from .views import (
    DepartamentoView,
    CarreraView,
    )

urlpatterns = [
    url(r'^departamento/$', DepartamentoView, name='departamento'),
    url(r'^carrera/$', CarreraView, name='carrera'),
    #url(r'^sobrenosotros/$', sobre, name='sobre'),

] 
