# Generated by Django 4.2.1 on 2023-05-27 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0003_remove_estado_cambioestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='cambioestado',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cambioEstados', to='encuestas.estado'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='nombre',
            field=models.CharField(default='Sin nombre', max_length=50),
        ),
    ]
