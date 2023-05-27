# Generated by Django 4.2.1 on 2023-05-27 05:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CambioEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('estado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cambioEstados', to='encuestas.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=10)),
                ('nombreCompleto', models.CharField(max_length=100)),
                ('nroCelular', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Llamada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('descripcionOperador', models.CharField(default='Sin descripcion', max_length=200)),
                ('detalleAccionRequerida', models.CharField(default='Sin detalle', max_length=200)),
                ('encuestaEnviada', models.BooleanField(default=False)),
                ('observacionAuditor', models.CharField(default='Sin observacion', max_length=200)),
                ('respuestasDeEncuesta', models.CharField(default='Sin respuestas', max_length=200)),
                ('cambioEstado', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='llamada', to='encuestas.cambioestado')),
                ('cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='llamada', to='encuestas.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaPosible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='Sin descripcion', max_length=100)),
                ('valor', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaDeCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuestasDeEncuesta', models.TextField()),
                ('fechaEncuesta', models.DateField()),
                ('llamada', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='respuestaDeCliente', to='encuestas.llamada')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(default='Sin descripcion', max_length=100)),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.respuestaposible')),
            ],
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaFinVigencia', models.DateField(default=datetime.datetime.now)),
                ('descripcion', models.CharField(default='Sin descripcion', max_length=100)),
                ('pregunta', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='encuestas.pregunta')),
            ],
        )
    ]
