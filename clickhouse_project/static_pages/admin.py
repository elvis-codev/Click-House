from django.contrib import admin
from .models import Usuario, Propiedad, Arrendatario, Arrendador

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo','rut','tipo_usuario')  
    list_filter = ('tipo_usuario',)  

    def nombre_completo(self, obj):
        return f"{obj.nombres} {obj.apellidos}"

    nombre_completo.short_description = 'Nombres'  


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comuna', 'tipo_inmueble', 'precio_arriendo')
    list_filter = ('comuna', 'tipo_inmueble')

@admin.register(Arrendatario)
class ArrendatarioAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

@admin.register(Arrendador)
class ArrendadorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cantidad_propiedades_publicadas')

    def cantidad_propiedades_publicadas(self, obj):
        return obj.propiedades_publicadas.count()
    cantidad_propiedades_publicadas.short_description = 'Propiedades publicadas'
