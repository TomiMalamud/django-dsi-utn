from django.db import models
from datetime import datetime

class Llamada(models.Model):
    duration = models.IntegerField(default = 0)
    descripcionOperador = models.CharField(max_length = 200, default = "Sin descripcion")
    detalleAccionRequerida = models.CharField(max_length = 200, default = "Sin detalle")
    encuestaEnviada = models.BooleanField(default = False)
    observacionAuditor = models.CharField(max_length=200, default = "Sin observacion")
    respuestasDeEncuesta = models.ManyToManyField("RespuestaDeCliente", related_name = 'llamada', default=None)
    cliente = models.ForeignKey("Cliente", on_delete = models.CASCADE, related_name = 'llamada', default=None)
    cambioEstado = models.ForeignKey("CambioEstado", on_delete=models.CASCADE, related_name ='llamada', default=None)

    def __str__(self):
        return f"Llamada: {self.duration} segundos"
    def esDePeriodo(start_date, end_date):
        llamadas = Llamada.objects.filter(
        cambioEstado__initial_datetime__range=[start_date, end_date],
        )
        return llamadas
    def determinarUltimoEstado(self):
        ultimo_cambio_estado = CambioEstado.objects.filter(llamada=self).order_by('-initial_datetime').first()
        if ultimo_cambio_estado:
            return ultimo_cambio_estado.estado
        else:
            return None
    
class Cliente(models.Model):
    dni = models.CharField(max_length=10)
    nombreCompleto = models.CharField(max_length=100)
    nroCelular = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombreCompleto}"

    def esCliente(self, dni):
        return self.dni == dni

    def getNombre(self):
        return self.nombreCompleto

class RespuestaDeCliente(models.Model):
    respuestasDeEncuesta = models.ForeignKey("RespuestaPosible", on_delete=models.CASCADE, related_name='respuestaDeCliente', default=None)
    fechaEncuesta = models.DateField()

    def __str__(self):
        return f"{self.respuestasDeEncuesta}"

class Estado(models.Model):
    nombre = models.CharField(max_length=50, default="Sin nombre")
    def __str__(self):
        return f"{self.nombre}"
    
    def esFinalizada(self):
        return self.nombre == "Finalizada"

    def esIniciada(self):
        return self.nombre == "Iniciada"

    def getNombre(self):
        return self.nombre

class CambioEstado(models.Model):
    initial_datetime = models.DateTimeField(default=datetime.now)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='cambioEstados', default=1)
    def __str__(self):
        return f"CambioEstado: {self.initial_datetime}"
    def getEstado(self):
        return self.estado
    
class RespuestaPosible(models.Model):
    descripcion = models.CharField(max_length=100, default="Sin descripcion")
    valor = models.IntegerField(default=0)

    def __str__(self):
        return f"Respuesta: {self.descripcion}"

    def getDescripcionRta(self):
        return self.descripcion

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=100, default="Sin descripcion")
    respuestas = models.ManyToManyField(RespuestaPosible,related_name='pregunta', default=None)

    def __str__(self):
        return f"Pregunta: {self.pregunta}"
    
    def getDescripcion(self):
        return self.pregunta

    def listarRespuestasPosibles(self):
        return self.respuestas

class Encuesta(models.Model):
    fechaFinVigencia = models.DateField(default=datetime.now)
    descripcion = models.CharField(max_length=100, default="Sin descripcion")
    pregunta = models.ManyToManyField(Pregunta, related_name='encuesta', default="None")

    def __str__(self):
        return f"Encuesta: {self.descripcion}"

    def armarEncuesta(self):
        pass

    def esEncuestaEnPeriodo(self):
        pass

    def esVigente(self):
        pass

    def getDescripcionEncuesta(self):
        return self.descripcion

    def getEncuestaPregunta(self):
        return self.pregunta
