from django.contrib import admin
from .models import *

# Register your models here.

class PeriodoProfesorModuloAdmin(admin.ModelAdmin):
    pass

admin.site.register(PeriodoProfesorModulo, PeriodoProfesorModuloAdmin)

