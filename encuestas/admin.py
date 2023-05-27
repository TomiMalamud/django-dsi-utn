from django.contrib import admin

from .models import Llamada, CambioEstado, RespuestaDeCliente, Cliente, Estado, RespuestaPosible

admin.site.register(Llamada)

admin.site.register(CambioEstado)

admin.site.register(RespuestaDeCliente)

admin.site.register(Cliente)

admin.site.register(Estado)

admin.site.register(RespuestaPosible)