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

        #CursosGrupo
        CursosGrupoListView,
        CursosGrupoCreateView,
        CursosGrupoUpdateView,
        CursosGrupoDeleteView,
        saveCursosGrupo,
        GetModuloEspejoGruposCurso,
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
        #CursosGrupo
        url(r'^cursosgrupo/$', CursosGrupoListView.as_view(), name='cursosgrupo'),
        url(r'^cursosgrupo/add/$', CursosGrupoCreateView.as_view(), name='cursosgrupo-add'),
        url(r'^cursosgrupo/edit/(?P<pk>\d+)/$', CursosGrupoUpdateView.as_view(), name='cursosgrupo-edit'),
        url(r'^cursosgrupo/(?P<pk>\d+)/delete/$', CursosGrupoDeleteView.as_view(), name='cursosgrupo-delete'),

        #Param
        url(r'^horario/param/get_plan/$', GetPlan, name='get-plan'),
        url(r'^horario/param/get_periodo/$', GetPeriodo, name='get-periodo'),
        url(r'^horario/param/get_profesor/$', GetProfesor, name='get-periodo'),
        url(r'^horario/param/get_modulo/$', GetModulo, name='get-modulo'),
        url(r'^horario/param/get_carrera/$', GetCarrera, name='get-carrera'),
        url(r'^horario/param/get_actividad/$', GetActividad, name='get-actividad'),

        #CursosGrupo
        url(r'^horario/param/get_carrera-cg/$', GetCarrera, name='get-carrera-cg'),
        url(r'^horario/param/get_plan-cg/$', GetPlan, name='get-plan-cg'),
        url(r'^horario/param/get_modulo-cg/$', GetModulo, name='get-modulo-cg'),
        url(r'^horario/cg/save/$', saveCursosGrupo, name='cursos-grupo-save'),

        #CursosGrupo y Espejo
        url(r'^horario/param/get_modulo_espejo_cursos_grupo/$',
            GetModuloEspejoGruposCurso, name='get-espejo-cg'),

        #validaciones
        url(r'^horario/horario/get_valida_ppm/$', GetValidaPpm, name='get-valida-ppm'),

        #delete Temp
        url(r'^horario/horario/delete_horario_temp/$', deleteHorarioTemp, name='delete-horariotemp'),
        ]
