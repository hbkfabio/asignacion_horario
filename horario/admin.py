from django.contrib import admin
from .models import *

# Register your models here.

class PeriodoProfesorModuloAdmin(admin.ModelAdmin):
    pass

admin.site.register(PeriodoProfesorModulo, PeriodoProfesorModuloAdmin)


class HorarioAdmin(admin.ModelAdmin):
    pass
admin.site.register(Horario, HorarioAdmin)


class ReservaBloqueProtegidoAdmin(admin.ModelAdmin):
    pass
admin.site.register(ReservaBloqueProtegido, ReservaBloqueProtegidoAdmin)
