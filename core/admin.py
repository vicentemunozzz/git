from django.contrib import admin

# Register your models here.

from .models import Persona, Region,Ciudad

# Register your models here.
#clase de configuracion para
#el automovil en el admin de django
class PersonaAdmin(admin.ModelAdmin):
    #declaramos una tupla
    list_display = ('run','nombre','correo', 'telefono', 'Region','Ciudad')
    search_fields = ['run', 'nombre']
    #agregaremos un filtro personalizado en el admin
    list_filter = ('Region',)

admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Persona,PersonaAdmin)
