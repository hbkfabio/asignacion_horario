from django.contrib import admin
from carrera.models import *

# Register your models here.


class CarreraAdmin(admin.ModelAdmin):
    pass

admin.site.register(Carrera, CarreraAdmin)

class PlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Plan, PlanAdmin)
