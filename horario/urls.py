from django.conf.urls import url
from .views import (PeriodoProfesorModuloListView,
                    PeriodoProfesorModuloCreateView,
                    PeriodoProfesorModuloUpdateView,
                    PeriodoProfesorModuloDeleteView,
                    # HorarioView,
                    HorarioTemplateView,
                    HorarioSave,
                    HorarioListView,
                    )

urlpatterns = [
    #Periodo Profesor Modulo
    url(r'^periodoprofesormodulo/$', PeriodoProfesorModuloListView.as_view(), name='periodoprofesormodulo'),
    url(r'^periodoprofesormodulo/add/$', PeriodoProfesorModuloCreateView.as_view(), name='periodoprofesormodulo-add'),
    url(r'^periodoprofesormodulo/edit/(?P<pk>\d+)/$', PeriodoProfesorModuloUpdateView.as_view(), name='periodoprofesormodulo-edit'),
    url(r'^periodoprofesormodulo/(?P<pk>\d+)/delete/$', PeriodoProfesorModuloDeleteView.as_view(), name='periodoprofesormodulo-delete'),
    #Horario
    url(r'^horario/$', HorarioListView.as_view(), name='horario'),
    url(r'^horario/edit/$', HorarioTemplateView.as_view(), name='horario-edit'),
    url(r'^horario/save/$', HorarioSave, name='horario-save'),

    ]
