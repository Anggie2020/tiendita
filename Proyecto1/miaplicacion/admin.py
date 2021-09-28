from django.contrib import admin
from miaplicacion.models import inicioSesion,movimientos,producto,tienda, usuario
# Register your models here.

admin.site.register(inicioSesion)
admin.site.register(movimientos)
admin.site.register(producto)
admin.site.register(tienda)
admin.site.register(usuario)