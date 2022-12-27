from django.contrib import admin
from .models import Inventario, Marca, Sucursal, Traslado, Ventas

# Register your models here.

class InventariosAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_reg',)

admin.site.register(Inventario, InventariosAdmin)
admin.site.register(Marca, InventariosAdmin)
admin.site.register(Sucursal, InventariosAdmin)
admin.site.register(Traslado, InventariosAdmin)
admin.site.register(Ventas, InventariosAdmin)
