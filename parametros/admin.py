from django.contrib import admin
from .models import *

# Register your models here.


class CarreraAdmin(admin.ModelAdmin):
    pass

admin.site.register(Carrera, CarreraAdmin)

class PlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Plan, PlanAdmin)

class ModuloAdmin(admin.ModelAdmin):
    pass

admin.site.register(Modulo, ModuloAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Departamento, DepartamentoAdmin)

class ProfesorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profesor, ProfesorAdmin)

class PeriodoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Periodo, PeriodoAdmin)

class AnioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Anio, AnioAdmin)


class BloqueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bloque, BloqueAdmin)
