from django.conf.urls import url
from .views import DepartamentoView

urlpatterns = [
    url(r'^departamento/$', DepartamentoView, name='departamento'),
    #url(r'^sobrenosotros/$', sobre, name='sobre'),

] 
