from django.contrib import admin

from .models import Llamada, CambioEstado, RespuestaDeCliente, Cliente, Estado, RespuestaPosible, Encuesta, Pregunta

admin.site.register(Llamada)

admin.site.register(CambioEstado)

admin.site.register(RespuestaDeCliente)

admin.site.register(Cliente)

admin.site.register(Estado)

admin.site.register(RespuestaPosible)

admin.site.register(Encuesta)

admin.site.register(Pregunta)