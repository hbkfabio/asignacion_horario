from django.conf.urls import url
from .views import (PeriodoProfesorModuloListView,
                    PeriodoProfesorModuloCreateView,
                    PeriodoProfesorModuloUpdateView,
                    PeriodoProfesorModuloDeleteView,

                    #params
                    GetPlan,
                    GetPeriodo,
                    GetProfesor,
                    GetModulo,
                    GetCarrera,
                    GetActividad,
                    SaveActividadBloque,
                    GetValidaPpm,

                    SaveHorarioProtegido,
                    deleteHorarioTemp,

                    # HorarioView,
                    HorarioTemplateView,
                    HorarioSave,
                    saveHorario,
                    HorarioListView,
                    ReservaBloqueProtegidoListView,
                    ReservaBloqueProtegidoCreateView,
                    ReservaBloqueProtegidoUpdateView,
                    ReservaBloqueProtegidoDeleteView,
                    )

urlpatterns = [
    #Periodo Profesor Modulo
    url(r'^periodoprofesormodulo/$', PeriodoProfesorModuloListView.as_view(), name='periodoprofesormodulo'),
    url(r'^periodoprofesormodulo/add/$', PeriodoProfesorModuloCreateView.as_view(), name='periodoprofesormodulo-add'),
    url(r'^periodoprofesormodulo/edit/(?P<pk>\d+)/$', PeriodoProfesorModuloUpdateView.as_view(), name='periodoprofesormodulo-edit'),
    url(r'^periodoprofesormodulo/(?P<pk>\d+)/delete/$', PeriodoProfesorModuloDeleteView.as_view(), name='periodoprofesormodulo-delete'),
    #Reserva Bloque Protegido
    url(r'^reservabloqueprotegido/$', ReservaBloqueProtegidoListView.as_view(), name='reservabloqueprotegido'),
    url(r'^reservabloqueprotegido/save/$', SaveHorarioProtegido, name='save-reservabloqueprotegido'),
    url(r'^reservabloqueprotegido/add/$', ReservaBloqueProtegidoCreateView.as_view(), name='reservabloqueprotegido-add'),
    # url(r'^reservabloqueprotegido/edit/(?P<pk>\d+)/$', ReservaBloqueProtegidoUpdateView.as_view(), name='reservabloqueprotegido-edit'),
    url(r'^reservabloqueprotegido/(?P<pk>\d+)/delete/$', ReservaBloqueProtegidoDeleteView.as_view(), name='reservabloqueprotegido-delete'),
    #Horario
    url(r'^horario/$', HorarioListView.as_view(), name='horario'),
    url(r'^horario/edit/$', HorarioTemplateView.as_view(), name='horario-edit'),
    #url(r'^horario/save/$', HorarioSave, name='horario-save'),
    url(r'^horario/save/$', saveHorario, name='horario-save'),
    #url(r'^horario/saveActividadBloque/$', SaveActividadBloque, name='actividadbloque-save'),


    #Param
    url(r'^horario/param/get_plan/$', GetPlan, name='get-plan'),
    url(r'^horario/param/get_periodo/$', GetPeriodo, name='get-periodo'),
    url(r'^horario/param/get_profesor/$', GetProfesor, name='get-periodo'),
    url(r'^horario/param/get_modulo/$', GetModulo, name='get-modulo'),
    url(r'^horario/param/get_carrera/$', GetCarrera, name='get-carrera'),
    url(r'^horario/param/get_actividad/$', GetActividad, name='get-actividad'),

    #validaciones
    url(r'^horario/horario/get_valida_ppm/$', GetValidaPpm, name='get-valida-ppm'),

    #delete Temp
    url(r'^horario/horario/delete_horario_temp/$', deleteHorarioTemp, name='delete-horariotemp'),
    ]
